contatos = []
permissão = "Y"

while permissão in ["y", "yes", "sim", "s", "Y", "YES", "S", "SIM"]:
    contatos.append(input("\nAdicionar um contato a lista: "))
    permissão = input("\nAdicionar novo contato? (Y/N): ")

print(f"\nSua lista de contatos é: {contatos}")
nome = input(f"\nDigite um nome para pesquisa: ")

# if nome in contatos:
#     print(f"\nO nome {nome} está na lista!\n")
# else:
#     print(f"\nO nome pesquisado não consta na lista registrada!\n")

i = 0
while i < len(contatos) and nome != contatos[i]:
    i += 1 
    if i == len(contatos):
        print(f"\nO nome pesquisado não consta na lista registrada!\n")
    else:
        print(f"\nO nome {nome} está na lista na posição {[i+1]}!\n")