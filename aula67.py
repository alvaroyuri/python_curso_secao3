"""Calculadora com While"""

while True:
    
    print ('Essa é sua calculadora Python')
                
    numero1 = input ('Por favor, digite o primeiro número da sua operação aritmética: ')
    numero2 = input ('Agora digite o segundo número da operação: ')
    operador = input ('Por fim, digite o operador (adição/subtração/mutiplicação/divisão): ')

    numero1 = int(numero1)
    numero2 = int(numero2)

    if operador == '*':
        calculo = numero1 * numero2
        print (f'O resultado é: {calculo}')

    elif operador == '/':   
        calculo = numero1 / numero2
        print (f'O resultado é: {calculo}')

    elif operador == '+':   
        calculo = numero1 + numero2
        print (f'O resultado é: {calculo}')

    else:
        calculo = numero1 - numero2
        print (f'O resultado é: {calculo}')

    sair = input ('Digite [s] para sair: ').lower().startswith('s')

    if sair:
        print ('Calculadora fechada com sucesso')
        break

   
   
   
