nota = float(input("\nDigite a nota do aluno: "))

if nota >= 9:
    nota = "A"
elif 8 <= nota:
    nota = "B"
elif 7<= nota:
    nota = "C"
elif 6<= nota:
    nota = "D"
elif nota <6 and nota > 0:
    nota = "E"
else:
    nota = "F"

print(f"\nSua nota é: {nota}\n")