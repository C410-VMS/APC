from IBGE_funções import *
import numpy as np
import matplotlib.pyplot as plt

lista = np.random.normal(loc= 1000, scale=500, size=100)
lista = lista.round(2)

print(f"Lista: {lista}")

med = media(lista)
print(f"\nMédia da lista: {med:.2f}\n")

desv = desvio_padrao(lista)
print(f"Desvio padrão da lista: {desv:.2f}\n")

num_descartados = [float(x) for x in outlier(lista)]
print(f"Números fora do desvio: {num_descartados}")

plt.plot(lista, marker = ".", color = "red", label = "Renda")
plt.show()