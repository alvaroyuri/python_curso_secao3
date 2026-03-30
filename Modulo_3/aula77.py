palavra_secreta = 'gorila'
letra = input ('Digite uma letra: ')
resultado = 0

if len(letra) > 1:
    print ('Digite apenas uma letra')
    
if letra in palavra_secreta:

    print ("Contém essa letra")

else:
    print ("Não contém essa letra")


