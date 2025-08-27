num = int(input("\nQual número? "))

print(f"Tabuada do {num}: \n")

i = 1
while i <= 100:
    resultado = num * i
    print(f"{num}x{i} = {resultado}")
    i += 1

print("\n")