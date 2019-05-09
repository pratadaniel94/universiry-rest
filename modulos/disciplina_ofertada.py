from flask import Blueprint, jsonify, request
from workers.operator_sqlite3 import *

disc_ofertada = Blueprint('disc_ofertada', __name__, url_prefix='/disc_ofertada')


@disc_ofertada.route('/<int:id>', methods=['GET', 'DELETE', 'PUT'])
@disc_ofertada.route('', methods=['GET', 'POST'])
def manipular_disc_ofertadas(id=None):
    disc_ofertadas = select_all('disciplinas_ofertadas')
    if request.method == "GET":
        if id == None:
            return jsonify(disc_ofertadas)

        for disc_ofertada in disc_ofertadas:
            if id == disc_ofertada['id']:
                return jsonify(disc_ofertada)
        else:
            return jsonify({"mensagem": "disciplina ofertada não cadastrado"}), 404

    if request.method == 'POST':
        data = request.json
        if data:
            keys = data.keys()
            if all(['id' in keys, 'id_disciplina' in keys,
                    'id_professor' in keys, 'ano' in keys, 'semestre' in keys,
                    'turma' in keys]):
                operator_sql("insert into disciplinas_ofertadas values ('{}','{}','{}','{}','{}','{}')".format(
                    data['id'], data['ano'],data['id_disciplina'],data['id_professor'],data['semestre'], data['turma']))
                return jsonify({"mensagem": "disciplina ofertada 'id {}'registrado com sucesso".format(data['id'])})
            else:
                return jsonify({"mensagem": "json invalid"}), 400
        else:
            return jsonify({"mensagem": "json invalid"}), 400

    if request.method == "DELETE":
        for disc_ofertada in disc_ofertadas:
            if id == disc_ofertada['id']:
                operator_sql("delete from disciplinas_ofertadas where id='{}'".format(id))
                return jsonify({"mensagem": "disciplina ofertada removido com sucesso!"})
        else:
            return jsonify({"mensagem": "disciplina ofertada não encontrado"}), 404

    if request.method == "PUT":
        data = request.json
        if data:
            keys = data.keys()
            if all(['id' in keys, 'id_disciplina' in keys,
                    'id_professor' in keys, 'ano' in keys, 'semestre' in keys,
                    'turma' in keys]):
                for disc_ofertada in disc_ofertadas:
                    if disc_ofertada['id'] == id:
                        operator_sql("update disciplinas set id='{}',ano='{}',id_disciplina='{}',id_professor='{}',semestre='{}',turma='{}' where id='{}'".format(id))
                        return jsonify({"mensagem": "disciplina ofertada atualizado com sucesso!"})
                else:
                    return jsonify({"mensagem": "disciplina ofertada não encontrado"}),404
            else:
                return jsonify({"mensagem": "json invalid"}), 400
        else:
            return jsonify({"mensagem": "json invalid"}), 400