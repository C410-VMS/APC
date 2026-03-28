lista = [1, 2, 3, 4, 5, 15, 50, 9, 10, 1, 100]
soma = 0
valor = int(input("\nDigite o valor: "))
i = 0

while i < len(lista) and soma <= valor:
    soma += lista[i]
    i += 1
    print(lista[i])

if soma > valor:
    print(f"A soma dos valores: {soma} é maior que {valor}\n")
elif soma == valor:
    print("Os valores da soma e indicado são iguais!\n")
else:
    print(f"A soma dos valores: {soma} não é maior que {valor}\n")