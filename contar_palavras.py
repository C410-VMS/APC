def cont_palavras(texto):
    import string
    texto = texto.translate(str.maketrans('', '', string.punctuation)).lower()
    texto_fatiado = texto.split()

    cont = {}

    for palavra in texto_fatiado:
        cont[palavra] = cont.get(palavra, 0) +1

    return cont

texto_exemplo = "O gato caça o rato. O rato foge do gato."
print(f'Texto exemplo: "{texto_exemplo}"')
texto = input("Digite o texto parar contagem de palavras, ou utilize o texto exemplo: ")

if not texto:
    resultado = cont_palavras(texto_exemplo)
    print(resultado)
else:
    resultado = cont_palavras(texto)
    print(resultado)