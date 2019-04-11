from flask import Blueprint, jsonify, request
from workers import read_json, write_json

disc_ofertada = Blueprint('disc_ofertada', __name__, url_prefix='/disc_ofertada')


@disc_ofertada.route('/<int:id>', methods=['GET', 'DELETE', 'PUT'])
@disc_ofertada.route('', methods=['GET', 'POST'])
def manipular_disc_ofertadas(id=None):
    disc_ofertadas = read_json('disciplinas_ofertadas')
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
                write_json('disciplinas_ofertadas', data)
                return jsonify({"mensagem": "disciplina ofertada 'id {}'registrado com sucesso".format(data['id'])})
            else:
                return jsonify({"mensagem": "json invalid"}), 400
        else:
            return jsonify({"mensagem": "json invalid"}), 400

    if request.method == "DELETE":
        for disc_ofertada in disc_ofertadas:
            if id == disc_ofertada['id']:
                write_json('disciplinas_ofertadas', disc_ofertada, 'remove')
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
                        write_json('disciplinas_ofertadas', disc_ofertada, acao='update', update=data)
                        return jsonify({"mensagem": "disciplina ofertada atualizado com sucesso!"})
                else:
                    return jsonify({"mensagem": "disciplina ofertada não encontrado"}),404
            else:
                return jsonify({"mensagem": "json invalid"}), 400
        else:
            return jsonify({"mensagem": "json invalid"}), 400