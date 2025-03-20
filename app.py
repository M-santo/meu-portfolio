from flask import Flask, render_template

app = Flask(__name__)

# Página inicial
@app.route('/')
def index():
    return render_template('index.html')

# Página sobre mim
@app.route('/sobre-me')
def about():
    return render_template('sobre-me.html')

# Página de projetos
@app.route('/projetos')
def projects():
    return render_template('projetos.html')

if __name__ == '__main__':
    app.run(debug=True)

