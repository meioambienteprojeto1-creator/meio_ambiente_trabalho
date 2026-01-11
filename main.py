import os

from flask import Flask, send_file, url_for, render_template, session, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
app = Flask(__name__)
app.secret_key = "chave-secreta-super-segura"

campanhas = [
    {
        "id": 0,
        "titulo": "Campanha de reciclagem do lixo",
        "data": "09/01/2026",
        "imagem": "imagens/reciclagem.png",
        "descricao": "Piripiri - Recicle corretamente e transforme o lixo em recursos. Cada ato consciente ajuda a reduzir o impacto no meio ambiente."
    },
    {
        "id": 1,
        "titulo": "Campanha de consumo consciente de água",
        "data": "09/01/2026",
        "imagem": "imagens/agua.png",
        "descricao": "Piripiri - Economize água! Pequenas atitudes no dia a dia garantem um futuro sustentável e preservam este recurso vital."
    },
    {
        "id": 2,
        "titulo": "Campanha para o plantio de árvores",
        "data": "09/01/2026",
        "imagem": "imagens/arvore.png",
        "descricao": "Piripiri - Ação ambiental para plantio de árvores e conscientização ecológica."
    }
]

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
    return render_template("index.html", campanhas=campanhas)
def main():
    app.run(port=int(os.environ.get('PORT', 80)), debug=True)


@app.route("/contato")
def contato():
    return render_template("contato.html")




@app.route('/favicon.ico')
def favicon():
    path = os.path.join(app.root_path, 'static', 'icons', 'favicon.ico')
    return send_file(path, mimetype='image/vnd.microsoft.icon')



@app.route("/campanha", methods=["GET"])
def campanha():
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
    if 0 <= id < len(campanhas):
        campanha_selecionada = campanhas[id]
    else:
        campanha_selecionada = None

    return render_template("descricao.html", campanha=campanha_selecionada)
















if __name__ == "__main__":
    main()
