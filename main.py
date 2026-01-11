import os

from flask import Flask, send_file, url_for, render_template, request

app = Flask(__name__)

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
