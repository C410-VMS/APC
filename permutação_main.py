from permutação import *

palavra1 = input("\nDigite a primeira palavra: ")
palavra2 = input("Digite a segunda palavra: ")

verdade = Permutação(palavra1,palavra2)

if verdade == True:
    print(f"\nAs palavras: {palavra1} e {palavra2} são permutações uma da outra!\n")
else:
    print(f"\nAs palavras: {palavra1} e {palavra2} NÃO são permutações uma da outra!\n")