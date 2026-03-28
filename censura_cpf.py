# cpf = "14434570439"

# print(cpf[:3]+"*****"+cpf[-3:])
valor = "1238126461348234813046"

valor_mask = valor[:3]
n_estrelas = len(valor) -6

for i in range(n_estrelas):
    valor_mask += "*"

valor_mask += valor[-3:]

print(f"\n{valor_mask}\n")