from flask import Flask, render_template
from modulos import *

app = Flask(__name__)
app.register_blueprint(aluno)
app.register_blueprint(professor)
app.register_blueprint(coord)
app.register_blueprint(disciplina)
app.register_blueprint(curso)
app.register_blueprint(disc_ofertada)
app.register_blueprint(matricula)




@app.route('/relatorio')
def hello_world():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
