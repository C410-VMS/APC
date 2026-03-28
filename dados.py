def agrupar(lista:list)->dict:
    setores = {}
    for tupla in lista:
        funcionario,setor = tupla
        if setor not in setores:
            setores[setor] = [funcionario]
        else:
            setores[setor].append(funcionario)
    return (setores)

dados = [
    ("João", "TI"),
    ("Maria", "RH"),
    ("Pedro", "TI"),
    ("Ana", "Financeiro"),
    ("Clara", "RH")
]

i = agrupar(dados)
print(i)