idade = int(input("\nDigite sua idade: "))

if idade < 14 and idade > 0:
    print("\nCriança\n")
elif idade >= 14 and idade < 18:
    print("\nAdolescente\n")
elif idade >= 18 and idade < 60:
    print("\nAdulto\n")
elif idade >= 60:
    print("\nIdoso\n")
else:
    print("\nValor inválido!\n")