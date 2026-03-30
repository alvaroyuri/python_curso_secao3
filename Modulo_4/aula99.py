
"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

mutiplicador = 10
cpf = '746.824.890-70'
cpf_tratado = cpf.replace('.', '').replace('-', '')[:9]
soma = 0

for i in range (9):
    mutiplicacao = int(cpf_tratado[i]) * mutiplicador
    soma += mutiplicacao 
    mutiplicador -= 1

digito1 = ((soma * 10) % 11)

if digito1 > 9:
    digito1 = 0

print ('Este é o digito 1: ', digito1)

#Segundo exercicio

mutiplicador = 11
cpf = '746.824.8907-70'
cpf_tratado = cpf.replace('.', '').replace('-', '')[:10]
soma = 0

for i in range (10):
    mutiplicacao = int(cpf_tratado[i]) * mutiplicador
    soma += mutiplicacao 
    mutiplicador -= 1

digito2 = ((soma * 10) % 11)

if digito2 > 9:
    digito2 = 0

print ('Este é o digito 2: ', digito2)



