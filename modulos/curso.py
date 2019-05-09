from flask import Blueprint, jsonify, request
from workers.operator_sqlite3 import *

curso = Blueprint('curso', __name__, url_prefix='/curso')

@curso.route('/<int:id>', methods=['GET', 'DELETE', 'PUT'])
@curso.route('', methods=['GET', 'POST'])
def manipular_cursos(id=None):
    cursos = select_all('cursos')
    if request.method == "GET":
        if id == None:
            return jsonify(cursos)

        for curso in cursos:
            if id == curso['id']:
                return jsonify(curso)
        else:
            return jsonify({"mensagem": "curso não cadastrado"}), 404

    if request.method == 'POST':
        data = request.json
        if data:
            if 'id' in data.keys() and 'nome' in data.keys():
                operator_sql("insert into cursos values ('{}','{}')".format(data['id'], data['nome']))
                return jsonify({"mensagem": "curso 'id {} nome: {}'registrado com sucesso".format(data['id'], data['nome'])})
            else:
                return jsonify({"mensagem": "json invalid"}), 400
        else:
            return jsonify({"mensagem": "json invalid"}), 400

    if request.method == "DELETE":
        for curso in cursos:
            if id == curso['id']:
                operator_sql("delete from cursos where id='{}'".format(id))
                return jsonify({"mensagem": "curso removido com sucesso!"})
        else:
            return jsonify({"mensagem": "curso não encontrado"}), 404

    if request.method == "PUT":
        data = request.json
        if data:
            if 'id' in data.keys() and 'nome' in data.keys():
                for curso in cursos:
                    if curso['id'] == id:
                        operator_sql("update cursos set nome='{}', id='{}' where id='{}'".format(data['nome'], data['id'], id))
                        return jsonify({"mensagem": "curso atualizado com sucesso!"})
                else:
                    return jsonify({"mensagem": "curso não encontrado"}),404
            else:
                return jsonify({"mensagem": "json invalid"}), 400
        else:
            return jsonify({"mensagem": "json invalid"}), 400