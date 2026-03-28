def Permutação(palavra1:str, palavra2:str)->bool:
    
    cont = 0

    for letra in palavra1:
        for i in palavra2:
            if i == letra:
                cont += 1 

    if cont == len(palavra2):
        return True
        
    return False 