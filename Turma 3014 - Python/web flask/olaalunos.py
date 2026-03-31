from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Olá, alunos! 🧡</h1>
    <img src="/static/python.jpg.jpg" width="300">
    """

if __name__== "__main__":
    app.run(debug=True)