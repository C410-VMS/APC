def contador(texto:str, palavra_buscada:str) -> int:
    texto_fatiado = texto.split()
    
    cont = 0

    for palavra in texto_fatiado:
        if palavra == palavra_buscada:
            cont += 1
    
    return print(f'A palavra que você buscou aparece {cont} vezes.')

texto = 'Muitos editores de texto possuem a função de contar a ocorrência de cada palavra no texto'

palavra_buscada = 'texto'

contador(texto, palavra_buscada)