def Copiar_sem_repetição(lista:list)->list:

    lista_saida = []

    for i in lista:
        if Verificar_existencia(lista_saida,i) == False:
            lista_saida.append(i)
    return lista_saida

def Verificar_existencia(lista:list, i:int)->bool:

    for n in lista:
        if n == i:
            return True
    return False 