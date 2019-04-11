from json import loads, dumps


def read_json(chave=None):
    if chave:
        with open('package.json', 'r') as arq:
            return loads(arq.read())[chave]
    else:
        with open('package.json', 'r') as arq:
            return loads(arq.read())


def write_json(recurso, data,  acao='append', update=None):
    conteudo = read_json()
    if acao == 'append':
        conteudo[recurso].append(data)
    elif acao == 'remove':
        conteudo[recurso].remove(data)
    elif acao == 'update':
        conteudo[recurso].remove(data)
        conteudo[recurso].append(update)
    with open('package.json', 'w') as arq:
        arq.write(dumps(conteudo))
