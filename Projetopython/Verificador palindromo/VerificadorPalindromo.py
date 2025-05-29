palavra = (input('digite uma palavra'))
palavra_invertida = palavra[::-1]

if(palavra == palavra_invertida):
   print('e um palindromo')

else:
    print("não e palindromo")
