nome = 'Alvaro Yuri'
qtd_letras = len(nome)
contador = 0
novo_nome = ''

while contador < qtd_letras:
    
    letra = nome[contador]
    novo_nome += f'*{letra}'
    contador += 1

print (novo_nome)