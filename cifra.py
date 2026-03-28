# alfabeto = "abcdefghijklmnopqrstuvwxyz"

# palavra = str(input("\nQual a plavra deve ser criptografada? "))
# key = int(input("Qual a chave da sifra? "))

# contador = -1

# if key == 0:
#     print(f"\n{palavra}... tá surpreso? ")

# elif key < 0:
#     print("\nSem chave negativa!")

# else:
#     for i in palavra:
#         for i_2 in alfabeto:
#             contador = contador + 1
#             if i == i_2:
#                 if contador + key > 26:
#                     contador = contador - 26
#                     print(alfabeto[contador + key - 1], end = "")
#                 else:
#                     print(alfabeto[contador + key - 1], end = "")
alfabeto = "abcdefghijklmnopqrstuvwxyz"

palavra = str(input("\nQual a plavra deve ser criptografada? "))
key = int(input("Qual a chave da sifra? "))
print("\n")

palavra_cifrada = ""

for letra in palavra:
    print(f"Processando letra: {letra}")
    p = 0
    for letra_alfa in alfabeto:
        if letra == letra_alfa:
            break
        p += 1
    print(f"Posição da letra {letra}: {p}")

    p = (p + key) % 26
    print(f"Nova posição: {p}")

    print(f"Letra correspondente: {alfabeto[p]}\n---")
    palavra_cifrada += alfabeto[p]

print(f"A palavra: {palavra}, passando pela cifra de César com chave {key}, é: {palavra_cifrada}\n")
