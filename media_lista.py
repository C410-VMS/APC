# numeros = [7.5,8,9.6,7.8,10]

# soma = 0

# for i in numeros:
#     if i >= 0:
#         soma += i

# media = soma / len(numeros)

# print(f"\n{media:.2f}\n")

numeros = [7.5,8,9.6,7.8,10]
cont = soma = 0

for i in numeros:
     if i >= 0:
         soma += i
         cont += 1

media = soma / cont
print(f"\n{media}\n")