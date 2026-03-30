


def mutiplicador (*args):
    total = 1
    for numero in args:
        total *= numero

    return total

resultado = mutiplicador (3, 3, 6, 7 , 8, 29)
print (resultado) 

def par_ou_impar (resultado):
    if resultado % 2 == 0:
        return 'É par'
    
    return 'É Impar'

par_ou_impar_resultado = par_ou_impar (resultado)
    
print (par_ou_impar_resultado)
