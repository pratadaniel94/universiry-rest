from flask import Blueprint, jsonify, request
from workers import read_json, write_json


coord = Blueprint('coordenador', __name__, url_prefix='/coordenador')

@coord.route('/<int:id>', methods=['GET', 'DELETE', 'PUT'])
@coord.route('', methods=['GET', 'POST'])
def manipular_alunos(id=None):
    coords = read_json('coordenadores')
    if request.method == "GET":
        if id == None:
            return jsonify(coords)

        for coord in coords:
            if id == coord['id']:
                return jsonify(coord)
        else:
            return jsonify({"mensagem": "coordenador não cadastrado"}), 404

    if request.method == 'POST':
        data = request.json
        if data:
            if 'id' in data.keys() and 'nome' in data.keys():
                write_json('coordenadores', data)
                return jsonify({"mensagem": "coordenador 'id {} nome: {}'registrado com sucesso".format(data['id'], data['nome'])})
            else:
                return jsonify({"mensagem": "json invalid"}), 400
        else:
            return jsonify({"mensagem": "json invalid"}), 400

    if request.method == "DELETE":
        for coord in coords:
            if id == coord['id']:
                write_json('coordenadores', coord, 'remove')
                return jsonify({"mensagem": "coordenador removido com sucesso!"})
        else:
            return jsonify({"mensagem": "coordenador não encontrado"}), 404

    if request.method == "PUT":
        data = request.json
        if data:
            if 'id' in data.keys() and 'nome' in data.keys():
                for coord in coords:
                    if coord['id'] == id:
                        write_json('coordenadores', coord, acao='update', update=data)
                        return jsonify({"mensagem": "coordenador atualizado com sucesso!"})
                else:
                    return jsonify({"mensagem": "coordenador não encontrado"}),404
            else:
                return jsonify({"mensagem": "json invalid"}), 400
        else:
            return jsonify({"mensagem": "json invalid"}), 400


