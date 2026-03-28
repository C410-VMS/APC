from math import sqrt

def media(numeros:list)->float:
    soma = 0
    for n in numeros:
        soma += n
    return round(soma/len(numeros))

def desvio_padrao(numeros:list)->float:
    med = media(numeros)
    soma = 0

    for n in numeros:
        soma += (n-med)**2
    return float(sqrt(soma/len(numeros)))

def outlier(numeros:list)->list:
    out = []
    med = media(numeros)
    desv = desvio_padrao(numeros)

    for n in numeros:
        if n < 2 * med + desv or n < (-1)*desv:
            out.append(n)
    return out