from flask import Blueprint, jsonify, request
from workers.operator_sqlite3 import *

aluno = Blueprint('aluno', __name__, url_prefix='/aluno')




@aluno.route('/<string:id>', methods=['GET', 'DELETE', 'PUT'])
@aluno.route('', methods=['GET', 'POST'])
def manipular_alunos(id=None):
    alunos = select_all('alunos')
    if request.method == "GET":
        if id == None:
            return jsonify(alunos)

        for aluno in alunos:
            if id == aluno['id']:
                return jsonify(aluno)
        else:
            return jsonify({"mensagem": "aluno não cadastrado"}), 404

    if request.method == 'POST':
        data = request.json
        if data:
            if 'id' in data.keys() and 'nome' in data.keys():
                operator_sql("insert into alunos values ('{}','{}')".format(data['id'], data['nome']))
                return jsonify({"mensagem": "Aluno 'id {} nome: {}'registrado com sucesso".format(data['id'], data['nome'])})
            else:
                return jsonify({"mensagem": "json invalid"}), 400
        else:
            return jsonify({"mensagem": "json invalid"}), 400

    if request.method == "DELETE":
        for aluno in alunos:
            if id == aluno['id']:
                operator_sql("delete from alunos where id='{}'".format(id))
                return jsonify({"mensagem": "aluno removido com sucesso!"})
        else:
            return jsonify({"mensagem": "aluno não encontrado"}), 404

    if request.method == "PUT":
        data = request.json
        if data:
            if 'id' in data.keys() and 'nome' in data.keys():
                for aluno in alunos:
                    if aluno['id'] == id:
                        operator_sql("update alunos set nome='{}', id='{}' where id='{}'".format(data['nome'], data['id'], id))
                        return jsonify({"mensagem": "aluno atualizado com sucesso!"})
                else:
                    return jsonify({"mensagem": "aluno não encontrado"}), 404
            else:
                return jsonify({"mensagem": "json invalid"}), 400
        else:
            return jsonify({"mensagem": "json invalid"}), 400


