def conta_vogais(texto:str)->dict:
    vogais = {
        "a":0,
        "e":0,
        "i":0,
        "o":0,
        "u":0,
    }

    for letra in texto:
        if letra in vogais:
            vogais[letra] += 1
    return vogais

texto = "Eu ouvia o iaiai aereo ecoar ao longe, uivando melodias etereas e inusitadas."
print(conta_vogais(texto))