from flask import Blueprint, jsonify, request
from workers import read_json, write_json

disciplina = Blueprint('disciplina', __name__, url_prefix='/disciplina')

@disciplina.route('/<int:id>', methods=['GET', 'DELETE', 'PUT'])
@disciplina.route('', methods=['GET', 'POST'])
def manipular_disciplina(id=None):
    disciplinas = read_json('disciplinas')
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
                   'plano_ensino' in keys, 'carga_horario' in keys]):
                write_json('disciplinas', data)
                return jsonify({"mensagem": "disciplina 'id {} nome: {}'registrado com sucesso".format(data['id'], data['nome'])})
            else:
                return jsonify({"mensagem": "json invalid"}), 400
        else:
            return jsonify({"mensagem": "json invalid"}), 400

    if request.method == "DELETE":
        for disciplina in disciplinas:
            if id == disciplina['id']:
                write_json('disciplinas', disciplina, 'remove')
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
                        write_json('disciplinas', disciplina, acao='update', update=data)
                        return jsonify({"mensagem": "disciplina atualizado com sucesso!"})
                else:
                    return jsonify({"mensagem": "disciplina não encontrado"}),404
            else:
                return jsonify({"mensagem": "json invalid"}), 400
        else:
            return jsonify({"mensagem": "json invalid"}), 400


