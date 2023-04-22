from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return "Olá Mundo"


@app.route('/saudacao')
def saudacao():
    return '''
        <h1>Bem vinda(o) a nossa primeira página</h1>
        <p>Este é o primeiro parágrafo da página</p>
    '''


@app.route('/usuario/<int:id>')
def usuario(id):
    usuarios = {
        123: "Rafael",
        154: "Ana"
    }

    nome = usuarios.get(id, None)

    if nome is None:
        return "Usuário não cadastrado"

    return nome


if __name__ == "__main__":
    app.run()
