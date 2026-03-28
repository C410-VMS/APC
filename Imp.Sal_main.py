from Imposto import Calcular_imposto
from Salário import Calcular_salario

pagamento = Calcular_salario(
    int(input("\nQuantidade de horas trabalhadas no mês: ")),
    float(input("Valor recebido por hora: "))
)

imposto = Calcular_imposto(pagamento)
salario = pagamento - imposto

print(f"\nPelas horas trabalhadas no mês, você recebera: R${pagamento}")
print(f"O valor do imposto de renda será: R${imposto:.2f}")
print(f"Seu sálario final após o imposto de renda será: R${salario}\n")