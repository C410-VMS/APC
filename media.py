nota1 = float(input("\nQual foi sua primeira nota? "))
nota2 = float(input("Qual foi sua segunda nota? "))
nota3 = float(input("Qual foi sua terceira nota? "))
nota4 = float(input("Qual foi sua quarta nota? "))

ab1 = (nota1+nota2)/2
ab2 = (nota3+nota4)/2

media_final = (ab1+ab2)/2

print(f"\nSua AB1 foi: {ab1}")
print(f"\nSua AB2 foi: {ab2}")
print(f"\nSua media final foi: {media_final}")

if media_final >= 7:
    print("APROVADO!\n")
else:
    print("REAVALIAÇÃO!\n")