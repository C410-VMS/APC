num = int(input("\nDigite um número: "))

num2 = num - 1
fat = num 

while num2 != 0:
    fat *= num2
    # num2 -+ 1
    num2 -= 1
    print(fat)

print(f"\nO resultado da fatoração do número {num} é: {fat}.\n")