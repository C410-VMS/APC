lista = [10, 2, 3, 4, 5, 6, 7, 8, 9]

menor = maior = lista[0]

for n in lista:
    if n > maior:
        maior = n
    elif n < menor:
        menor = n

amplitude = maior - menor 

print(amplitude)