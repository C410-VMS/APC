num1 = int(input("\nDigite o número A: "))
num2 = int(input("Digite o número B: "))

if num1 > num2:
    print(f"\n{num1} é o maior número\n")
elif num2 > num1:
    print(f"\n{num2} é o maior número\n")
else:
    print("Os números são iguais.")