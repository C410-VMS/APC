x = int(input("\nAté qual número vai a contagem? ","\n"))

for y in range (0,x+1):
    if y !=0 and y %2 == 0: 
        print(y)
print(f"\nEsses são todos os números pares entre 0 e {x}\n")

# min = int(input("\nPrimeiro número da sequência: "))
# max = int(input("Último número da sequência: "))

# contador = 0

# if min > max:
#     print("Inválido!")

# for i in range(min, max+1):

#     if i !=0 and i %2 == 0:
#         contador +=1 

# print(f"\nExistem, {contador} números pares entre {min} e {max}\n")