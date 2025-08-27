a = int(input("\nQual o primeiro número da sequência? "))
b = int(input("Qual o último número da sequência? "))

soma = 0

if a > b:
    print("Inválido!")

for i in range(a,b+1):
    soma += i

print(f"\nA soma de todos os números entre {a} e {b} é: {soma}\n")