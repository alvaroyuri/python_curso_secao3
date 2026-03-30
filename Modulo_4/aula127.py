perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

for i in perguntas:

    print (i['Pergunta'])
    print (f'1) {i['Opções'][0]}')
    print (f'2) {i['Opções'][1]}')
    print (f'3) {i['Opções'][2]}')
    print (f'4) {i['Opções'][3]}')

   #Subtrai um e converte para interiro, para fazer o bate com a resposta (indice da resposta)
    try:
        resposta_user = int(input('Qual a opção correta? '))-1
        resposta_user = i['Opções'][resposta_user]
        resposta_correta = i['Resposta']

        if resposta_user == resposta_correta:
            print ('Resposta correta')
        else: 
            print ('Incorreto!')
    
    except ValueError:
        print ('Erro de valor')
    except IndexError:
        print ('Erro de Index')
