venda = float(input("\nValor de vendas: "))

if venda > 29999 and venda < 50000:
    comissão = venda * 0.095
    total = venda + comissão
    print(f"\nSeu ganho total foi de: R${total}\n")

elif venda > 50000:
    comissão = venda * 0.12
    total = venda + comissão
    print(f"\nSeu ganho total foi de: R${total}\n")

else:
    comissão = venda * 0.07
    total = venda + comissão
    print(f"\nSeu ganho total foi de: R${total}\n")