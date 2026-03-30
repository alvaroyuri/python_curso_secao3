nome = "Alvaro Yuri"
altura = 1.65
peso = 70
imc = peso / altura ** 2

#f-strings - Utilizado para formatação de strings
linha_1 = f'Meu nome é {nome} IMC:{imc:.2f}'
print (f'Meu nome é {nome}', f'IMC:{imc:.2f}')
print (linha_1)


#format - método format, utilizado para formatação de strings
a = 'AAAAA'
b = 'BBBBBB'
c = 1.1
string = 'b={nome2} a={nome1} a={nome1} c={nome3:.2f}'
formato = string.format(
    nome1=a, nome2=b, nome3=c
)

print(formato)