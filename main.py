import os
import firebase_admin

from firebase_admin import credentials, firestore
from flask import Flask, send_file, url_for, render_template, session, request, flash, redirect
from flask_mail import Mail, Message
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "chave-secreta-super-segura"

# Configurações do Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'meioambienteprojeto1@gmail.com'  # Seu email
app.config['MAIL_PASSWORD'] = 'segredo'  # Senha de app do Gmail
app.config['MAIL_DEFAULT_SENDER'] = 'meioambienteprojeto1@gmail.com'

mail = Mail(app)


cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

def get_campanhas():
    campanhas = []

    docs = (
        db.collection("campanhas")
        .order_by("id")
        .stream()
    )

    for doc in docs:
        campanha = doc.to_dict()
        campanhas.append(campanha)

    return campanhas


usuarios = {
    "admin": {
        "senha": generate_password_hash("1234")
    },
    "usuario": {
        "senha": generate_password_hash("senha123")
    }
}

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username in usuarios and check_password_hash(usuarios[username]["senha"], password):
            session["usuario"] = username
            flash("Login realizado com sucesso!", "success")
            return render_template("index.html", campanhas=campanhas)
        else:
            flash("Usuário ou senha incorretos", "danger")

    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("usuario", None)
    flash("Você saiu da conta", "info")
    return render_template("index.html", campanhas=campanhas)


@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        confirmar = request.form["confirmar"]

        # Verifica se o usuário já existe
        if username in usuarios:
            flash("Usuário já existe! Escolha outro.", "danger")
            return render_template("cadastro.html")

        # Verifica se as senhas conferem
        if password != confirmar:
            flash("As senhas não conferem.", "danger")
            return render_template("cadastro.html")

        # Cria o usuário com senha hash
        usuarios[username] = {"senha": generate_password_hash(password)}
        flash("Cadastro realizado com sucesso! Faça login.", "success")
        return render_template("login.html")

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