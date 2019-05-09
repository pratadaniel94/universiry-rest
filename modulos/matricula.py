from flask import Blueprint, jsonify, request
from workers.operator_sqlite3 import *

matricula = Blueprint('matricula', __name__, url_prefix='/matricula')

@matricula.route('/<int:id>', methods=['GET', 'DELETE', 'PUT'])
@matricula.route('', methods=['GET', 'POST'])
def manipular_matricula(id=None):
    matriculas = select_all('solicitacoes_matricula')
    if request.method == "GET":
        if id == None:
            return jsonify(matriculas)

        for matricula in matriculas:
            if id == matricula['id']:
                return jsonify(matricula)
        else:
            return jsonify({"mensagem": "solicitacao de atricula não cadastrado"}), 404

    if request.method == 'POST':
        data = request.json
        if data:
            keys = data.keys()
            if all(['id' in keys, 'id_aluno' in keys,
                    'id_disciplina_ofertada' in keys, 'dt_solicitacao' in keys,
                    'id_coordenador' in keys, 'status' in keys]):
                operator_sql("insert into solicitacoes_matricula values ('{}','{}','{}','{}','{}','{}')".format(
                    data['id'], data['id_aluno'],data['id_disciplina_ofertada'], data['dt_solicitacao'],
                data['id_coordenador'], data['status']))
                return jsonify({"mensagem": "solicitacao 'id {}' registrado com sucesso".format(data['id'])})
            else:
                return jsonify({"mensagem": "json invalid"}), 400
        else:
            return jsonify({"mensagem": "json invalid"}), 400

    if request.method == "DELETE":
        for matricula in matriculas:
            if id == matricula['id']:
                operator_sql("delete from solicitacoes_matricula where id='{}'".format(id))
                return jsonify({"mensagem": "matricula removido com sucesso!"})
        else:
            return jsonify({"mensagem": "matricula não encontrado"}), 404

    if request.method == "PUT":
        data = request.json
        if data:
            keys = data.keys()
            if all(['id' in keys, 'id_aluno' in keys,
                    'id_disciplina_ofertada' in keys, 'dt_solicitacao' in keys,
                    'id_coordenador' in keys, 'status' in keys]):
                for matricula in matriculas:
                    if matricula['id'] == id:
                        operator_sql("update disciplinas set id='{}',id_aluno='{}',id_disciplina_ofertada='{}',dt_solicitacao='{}',id_coordenador='{}',status='{}' where id='{}'".format(id))
                        return jsonify({"mensagem": "solicitacao matricula atualizado com sucesso!"})
                else:
                    return jsonify({"mensagem": "solicitacao matricula não encontrado"}),404
            else:
                return jsonify({"mensagem": "json invalid"}), 400
        else:
            return jsonify({"mensagem": "json invalid"}), 400