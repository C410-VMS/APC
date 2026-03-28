def contagem(lista)->dict:

    resultado = {}

    for i in lista:
        cont = lista.count(i)
        resultado[i] = (cont)

    return resultado

lista = [2,4,4,4,6,6,6,6,6,8,8,8,8,8,8,8,10,10,10,10,10,10,10,10,10]

dicionario = contagem(lista)
print(f"Essa é a contagem geral dos números: {dicionario}")