temp_f = float(input("\nQual a temperatura em ºF? "))

temp_c = (5/9) * (temp_f - 32)

temp_k = temp_c + 273.15

print(f"\nA temperatura em Fahrenheit é: {temp_f}ºF.")
print(f"A temperatura em Celsius é: {temp_c:.0f}ºC.")
print(f"A temperatura em Kelvin é: {temp_k:.0f}K.\n")
