from flask import Blueprint, jsonify, request
from workers import read_json, write_json

professor = Blueprint('professor', __name__, url_prefix='/professor')

@professor.route('/<int:id>', methods=['GET', 'DELETE', 'PUT'])
@professor.route('', methods=['GET', 'POST'])
def manipular_professores(id=None):
    professsores = read_json('professores')
    if request.method == "GET":
        if id == None:
            return jsonify(professsores)

        for prof in professsores:
            if id == prof['id']:
                return jsonify(prof)
        else:
            return jsonify({"mensagem": "professsor não cadastrado"}), 404

    if request.method == 'POST':
        data = request.json
        if data:
            keys = data.keys()
            if 'id' in keys and 'nome' in keys and 'matricula' in keys:
                write_json('professores', data)
                return jsonify(
                    {"mensagem": "Professor 'id {} nome: {}'registrado com sucesso".format(data['id'], data['nome'])})
            else:
                return jsonify({"mensagem": "json invalid"}), 400
        else:
            return jsonify({"mensagem": "json invalid"}), 400

    if request.method == "DELETE":
        for prof in professsores:
            if id == prof['id']:
                write_json('professores', prof, 'remove')
                return jsonify({"mensagem": "professor removido com sucesso!"})
        else:
            return jsonify({"mensagem": "professor não encontrado"}), 404

    if request.method == "PUT":
        data = request.json
        if data:
            keys = data.keys()
            if 'id' in keys and 'nome' in keys and 'matricula' in keys:
                for prof in professsores:
                    if prof['id'] == id:
                        write_json('professores', prof, acao='update', update=data)
                        return jsonify({"mensagem": "professor atualizado com sucesso!"})
                else:
                    return jsonify({"mensagem": "professor não encontrado"}), 404
            else:
                return jsonify({"mensagem": "json invalid"}), 400
        else:
            return jsonify({"mensagem": "json invalid"}), 400
