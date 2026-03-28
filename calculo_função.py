def soma(a:int,b:int)->int:
    if a != None and b != None:
        resultado = a + b
        return resultado
    return None 

def divisao(a,b):
    if b == 0:
        return None 
    resultado = a/b
    return resultado 

print(soma(5,4))
print(divisao(100,10))