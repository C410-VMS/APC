agenda = [
    "Anna",
    "Zago",
    "Elias",
    "Vitor",
    "Bernardo",
    "Enzo",
    "Lucas",
    "Edu"
]
nome = input("\nDigite um nome para pesquisa: ").lower

i = 0

while i < len(agenda) and nome != agenda[i]:
    i += 1

if i == len(agenda):
    print(f"O nome {nome} não está na lista!\n")
else:
    print(f"O nome {nome} está na lista!\n")