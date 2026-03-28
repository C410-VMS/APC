alunos = {}
nome = '_'

while nome != '':
    nome = input('Digite um nome:\n').capitalize()
    if nome != '':
        nota1 = float(input('Digite a primeira nota:\n'))
        nota2 = float(input('Digite a segunda nota:\n'))

        alunos[nome] = (nota1, nota2)

    else:
        nome_busca = input('Digite um nome para a busca:\n').capitalize()

        if nome_busca in alunos:
            media = (alunos[nome_busca][0] + alunos[nome_busca][1]) / 2
            print(f'A média de {nome_busca} foi {media}')