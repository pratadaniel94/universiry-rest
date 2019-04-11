from flask import Blueprint, jsonify, request
from workers import read_json, write_json

aluno = Blueprint('aluno', __name__, url_prefix='/aluno')


@aluno.route('/<int:id>', methods=['GET', 'DELETE', 'PUT'])
@aluno.route('', methods=['GET', 'POST'])
def manipular_alunos(id=None):
    alunos = read_json('alunos')
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
                write_json('alunos', data)
                return jsonify({"mensagem": "Aluno 'id {} nome: {}'registrado com sucesso".format(data['id'], data['nome'])})
            else:
                return jsonify({"mensagem": "json invalid"}), 400
        else:
            return jsonify({"mensagem": "json invalid"}), 400

    if request.method == "DELETE":
        for aluno in alunos:
            if id == aluno['id']:
                write_json('alunos', aluno, 'remove')
                return jsonify({"mensagem": "aluno removido com sucesso!"})
        else:
            return jsonify({"mensagem": "aluno não encontrado"}), 404

    if request.method == "PUT":
        data = request.json
        if data:
            if 'id' in data.keys() and 'nome' in data.keys():
                for aluno in alunos:
                    if aluno['id'] == id:
                        write_json('alunos', aluno, acao='update', update=data)
                        return jsonify({"mensagem": "aluno atualizado com sucesso!"})
                else:
                    return jsonify({"mensagem": "aluno não encontrado"}),404
            else:
                return jsonify({"mensagem": "json invalid"}), 400
        else:
            return jsonify({"mensagem": "json invalid"}), 400


