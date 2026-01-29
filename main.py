import os
import firebase_admin

from firebase_admin import credentials, firestore, storage
from flask import Flask, send_file, url_for, render_template, session, request, flash, redirect
from flask_mail import Mail, Message
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from datetime import datetime

app = Flask(__name__)
app.secret_key = "chave-secreta-super-segura"

# Configurações do Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'seu-email@gmail.com'
app.config['MAIL_PASSWORD'] = 'sua-senha-de-app'
app.config['MAIL_DEFAULT_SENDER'] = 'seu-email@gmail.com'

# Configurações de upload
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp'}

mail = Mail(app)

# Inicializar Firebase
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'storageBucket': 'seu-projeto.firebasestorage.app'  # ALTERE AQUI
})
db = firestore.client()
bucket = storage.bucket()

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def upload_imagem_firebase(file, filename):
    """Upload de imagem para Firebase Storage"""
    try:
        # Criar nome único para o arquivo
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        nome_arquivo = f"campanhas/{timestamp}_{secure_filename(filename)}"
        
        # Upload para Firebase Storage
        blob = bucket.blob(nome_arquivo)
        blob.upload_from_file(file, content_type=file.content_type)
        
        # Tornar público
        blob.make_public()
        
        # Retornar URL pública
        return blob.public_url
    except Exception as e:
        print(f"Erro no upload: {e}")
        return None

def get_campanhas():
    campanhas = []

    docs = (
        db.collection("conteudo")
        .order_by("id")
        .stream()
    )

    for doc in docs:
        campanha = doc.to_dict()
        campanhas.append(campanha)

    return campanhas


@app.route("/login", methods=["GET", "POST"])
def login():
    campanhas = get_campanhas()
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        # Buscar usuário no Firestore pelo email
        usuarios_ref = db.collection("usuarios")
        query = usuarios_ref.where("email", "==", email).limit(1).stream()
        
        usuario_encontrado = None
        for doc in query:
            usuario_encontrado = doc.to_dict()
            usuario_encontrado['id'] = doc.id
            break

        if usuario_encontrado and check_password_hash(usuario_encontrado["senha"], password):
            session["usuario"] = usuario_encontrado["nome"]
            session["usuario_id"] = usuario_encontrado["id"]
            session["usuario_email"] = usuario_encontrado["email"]
            flash("Login realizado com sucesso!", "success")
            return render_template("index.html", campanhas=campanhas)
        else:
            flash("Email ou senha incorretos", "danger")

    return render_template("login.html")

@app.route("/logout")
def logout():
    campanhas = get_campanhas()
    session.pop("usuario", None)
    session.pop("usuario_id", None)
    session.pop("usuario_email", None)
    flash("Você saiu da conta", "info")
    return render_template("index.html", campanhas=campanhas)


@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":
        nome = request.form["nome"]
        email = request.form["email"]
        password = request.form["password"]
        confirmar = request.form["confirmar"]

        # Verifica se a senha tem pelo menos 4 dígitos
        if len(password) < 4:
            flash("A senha deve ter pelo menos 4 caracteres.", "danger")
            return render_template("cadastro.html")

        # Verifica se o email já existe no Firestore
        usuarios_ref = db.collection("usuarios")
        query = usuarios_ref.where("email", "==", email).limit(1).stream()
        
        email_existe = False
        for doc in query:
            email_existe = True
            break

        if email_existe:
            flash("Email já cadastrado! Use outro email.", "danger")
            return render_template("cadastro.html")

        # Verifica se as senhas conferem
        if password != confirmar:
            flash("As senhas não conferem.", "danger")
            return render_template("cadastro.html")

        # Cria o usuário no Firestore
        try:
            novo_usuario = {
                "nome": nome,
                "email": email,
                "senha": generate_password_hash(password)
            }
            
            # Adiciona ao Firestore (o ID será gerado automaticamente)
            doc_ref = usuarios_ref.add(novo_usuario)
            
            flash("Cadastro realizado com sucesso! Faça login.", "success")
            return redirect(url_for('login'))
        
        except Exception as e:
            flash(f"Erro ao realizar cadastro. Tente novamente.", "danger")
            print(f"Erro ao cadastrar usuário: {str(e)}")
            return render_template("cadastro.html")

    return render_template("cadastro.html")

@app.route("/")
def index():
    campanhas = get_campanhas()
    return render_template("index.html", campanhas=campanhas)

def main():
    app.run(port=int(os.environ.get('PORT', 80)), debug=True)


@app.route("/contato", methods=["GET", "POST"])
def contato():
    if request.method == "POST":
        nome = request.form.get("Nome")
        email = request.form.get("Email")
        mensagem = request.form.get("Mensagem")
        
        try:
            # Criar mensagem de email
            msg = Message(
                subject=f"Contato do site - {nome}",
                recipients=['meioambienteprojeto1@gmail.com'],
                body=f"""
Nova mensagem recebida do formulário de contato:

Nome: {nome}
Email: {email}

Mensagem:
{mensagem}
                """,
                reply_to=email
            )
            
            # Enviar email
            mail.send(msg)
            flash("Mensagem enviada com sucesso! Entraremos em contato em breve.", "success")
            
        except Exception as e:
            flash(f"Erro ao enviar mensagem. Tente novamente mais tarde.", "danger")
            print(f"Erro ao enviar email: {str(e)}")
        
        return redirect(url_for('contato'))
    
    return render_template("contato.html")


@app.route('/favicon.ico')
def favicon():
    path = os.path.join(app.root_path, 'static', 'icons', 'favicon.ico')
    return send_file(path, mimetype='image/vnd.microsoft.icon')


@app.route("/campanha", methods=["GET"])
def campanha():
    campanhas = get_campanhas()
    query = request.args.get("q", "").lower()

    if query:
        resultados = [
            c for c in campanhas
            if query in c["titulo"].lower() or query in c["descricao"].lower()
        ]
    else:
        resultados = campanhas

    return render_template("campanha.html", resultados=resultados, query=query)


@app.route("/criar_campanha", methods=["GET", "POST"])
def criar_campanha():
    # Verificar se o usuário está logado
    if "usuario" not in session:
        flash("Você precisa estar logado para criar uma campanha.", "warning")
        return redirect(url_for("login"))
    
    if request.method == "POST":
    
        titulo = request.form.get("titulo")
        descricao = request.form.get("descricao")
        descricao_avancada = request.form.get("descricao_avancada")
        imagem = request.form.get("imagem")

        # Validações
        if not titulo or not descricao:
            flash("Título e descrição são obrigatórios.", "danger")
            return render_template("criar_campanha.html")
        
        try:
            campanhas_ref = db.collection("conteudo")
            docs = list(
                campanhas_ref
                .order_by("id", direction=firestore.Query.DESCENDING)
                .limit(1)
                .stream()
            )
            
            proximo_id = 0
            if docs:
                ultimo_doc = docs[0].to_dict()
                proximo_id = ultimo_doc.get("id", 0) + 1
            
            nova_campanha = {
                "id": proximo_id,
                "titulo": titulo,
                "descricao": descricao,
                "descricao_avancada": descricao_avancada,
                "data": datetime.now().strftime("%d/%m/%Y"),
                "autor": session["usuario"],
                "autor_email": session["usuario_email"],
                "imagem": imagem
            }
            
            campanhas_ref.add(nova_campanha)
            
            flash("Campanha criada com sucesso! 🎉", "success")
            
            # 🔥 REDIRECIONA PARA O INDEX
            return redirect(url_for("index"))
            
        except Exception as e:
            flash("Erro ao criar campanha. Tente novamente.", "danger")
            print(f"Erro ao criar campanha: {str(e)}")
            return render_template("criar_campanha.html")
    
    return render_template("criar_campanha.html")



@app.route("/descricao/<int:id>")
def descricao(id):
    campanhas = get_campanhas()
    if 0 <= id < len(campanhas):
        campanha_selecionada = campanhas[id]
    else:
        campanha_selecionada = None

    return render_template("descricao.html", campanha=campanha_selecionada)


if __name__ == "__main__":
    main()
