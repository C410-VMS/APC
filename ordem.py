num1 = int(input("\nDigite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

if (num1 <= num2 <= num3):
    print(f"\n{num1}, {num2}, {num3}\n")

elif (num1 <= num3 <= num2):
    print(f"\n{num1}, {num3}, {num2}\n")

elif (num2 <= num1 <= num3):
    print(f"\n{num2}, {num3}, {num1}\n")

elif (num2 <= num3 <= num1):
    print(f"\n{num2}, {num1}, {num3}\n")

elif (num3 <= num2 <= num1):
    print(f"\n{num3}, {num1}, {num2}\n")

elif (num3 <= num1 <= num2):
    print(f"\n{num3}, {num2}, {num1}\n")

else:
    print(f"\n{num1}, {num2}, {num3}\n")