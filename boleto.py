valor = float(input("\nDigite o valor do boleto: "))
dias = int(input("Digite a quantidade de dias em atraso: "))
multa = 2
juros = 0.05 

total = valor + multa + (valor*juros*dias)

print(f"\nValor final: {total}\n")