import os

from flask import Flask, send_file, url_for, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
def main():
    app.run(port=int(os.environ.get('PORT', 80)), debug=True)


@app.route("/contato")
def contato():
    return render_template("contato.html")
if __name__ == "__main__":
    main()
