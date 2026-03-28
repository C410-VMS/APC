cartela_bingo = {
    "B": [6,5,8,15,9],
    "I": [23,19,29,30,28],
    "N": [31,34,None,39,40],
    "G": [55,50,48,49,47],
    "O": [65,53,68,67,75]
}

sorteio = {6,35,49,100,5,50,91,8,75,42,11,15,34,66,22,51,9}

B = set(cartela_bingo["B"])
I = set(cartela_bingo["I"])
N = set(cartela_bingo["N"])
G = set(cartela_bingo["G"])
O = set(cartela_bingo["O"])

if B.issubset(sorteio):
    print(f"Bingo! Cartela vencedora pela coluna B: {B}")
elif I.issubset(sorteio):
    print(f"Bingo! Cartela vencedora pela coluna I: {I}")
elif N.issubset(sorteio):
    print(f"Bingo! Cartela vencedora pela coluna N: {N}")
elif G.issubset(sorteio):
    print(f"Bingo! Cartela vencedora pela coluna G: {G}")
elif O.issubset(sorteio):
    print(f"Bingo! Cartela vencedora pela coluna O: {O}")
else:
    print("Que pena! A cartela não venceu dessa vez.")

# Saída versão Deepseek: 

# for coluna, numeros in cartela_bingo.items():
#     acertos = [num for num in numeros if num in sorteio]

#     print(f"Coluna {coluna}: {numeros} → Acertos: {len(acertos)}/5")
#     if len(acertos) == 5:
#         print(f"BINGO! Coluna {coluna} completa!\n")
