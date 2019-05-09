from flask import Blueprint, jsonify, request
from workers.operator_sqlite3 import *

disciplina = Blueprint('disciplina', __name__, url_prefix='/disciplina')

@disciplina.route('/<int:id>', methods=['GET', 'DELETE', 'PUT'])
@disciplina.route('', methods=['GET', 'POST'])
def manipular_disciplina(id=None):
    disciplinas = select_all('disciplinas')
    if request.method == "GET":
        if id == None:
            return jsonify(disciplinas)

        for disciplina in disciplinas:
            if id == disciplina['id']:
                return jsonify(disciplina)
        else:
            return jsonify({"mensagem": "disciplina não cadastrado"}), 404

    if request.method == 'POST':
        data = request.json
        if data:
            keys = data.keys()
            if all(['id' in keys, 'nome' in keys,
                   'data' in keys,'status' in keys, 'id_coordenador' in keys,
                   'plano_ensino' in keys, 'carga_horaria' in keys]):
                operator_sql("insert into disciplinas values ('{}','{}','{}','{}','{}','{}','{}')".format(
                    data['id'], data['nome'], data['carga_horaria'], data['data'], data['id_coordenador'],
                    data['plano_ensino'], data['status']))
                return jsonify({"mensagem": "disciplina 'id {} nome: {}'registrado com sucesso".format(data['id'], data['nome'])})
            else:
                return jsonify({"mensagem": "json invalid"}), 400
        else:
            return jsonify({"mensagem": "json invalid"}), 400

    if request.method == "DELETE":
        for disciplina in disciplinas:
            if id == disciplina['id']:
                operator_sql("delete from disciplinas where id='{}'".format(id))
                return jsonify({"mensagem": "disciplina removido com sucesso!"})
        else:
            return jsonify({"mensagem": "disciplina não encontrado"}), 404

    if request.method == "PUT":
        data = request.json
        if data:
            keys = data.keys()
            if all(['id' in keys, 'nome' in keys,
                    'data' in keys, 'status' in keys, 'id_coordenador' in keys,
                    'plano_ensino' in keys, 'carga_horario' in keys]):
                for disciplina in disciplinas:
                    if disciplina['id'] == id:
                        operator_sql("update disciplinas set id='{}',nome='{}',carga_horaria='{}',data='{}',id_coordenador='{}',plano_ensino='{}',status='{}' where id='{}'".format(id))
                        return jsonify({"mensagem": "disciplina atualizado com sucesso!"})
                else:
                    return jsonify({"mensagem": "disciplina não encontrado"}),404
            else:
                return jsonify({"mensagem": "json invalid"}), 400
        else:
            return jsonify({"mensagem": "json invalid"}), 400


