real = float(input("\nQual o valor em Real? "))
tx_c = float(input("Qual a Taxa de Câmbio do dia? "))
dolar = real/tx_c

print(f"\nCom a taxa: {tx_c}, seu valor em Dollar é: ${dolar:.2f}\n")