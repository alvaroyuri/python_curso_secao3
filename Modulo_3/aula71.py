frase = 'O Python é uma linguagem de programação multiparadigma. ' \
    'Python foi criado por Guido van Rossum.'


frase = frase.lower().replace(" ", "")
qtd_letras = len(frase)
qtd_maior_letra = 0
indice = 0

while indice < qtd_letras:

    letra = frase[indice]
    check_qtd =  frase.count(letra)
    
    if check_qtd > qtd_maior_letra:

        maior_letra = letra
        qtd_maior_letra = check_qtd
    
    indice += 1


print (maior_letra, qtd_maior_letra)
