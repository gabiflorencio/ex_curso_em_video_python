
x = 18%2 #O resto da divisão entre 18 e 2
y = pow(2,2) #A potencia de 2 por 2 utilizando uma função
z = 2**2 #A potencia de 2 por 2 utilizando operador aritmético

print(x, y, z) 

#Posso fazer operações aritméticas entre strings e inteiros

print('Olá'*5) 

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))

print(f'A soma vale {n1 + n2}') #Posso fazer operações dentro da máscara.

s = n1 + n2
m = n1 * n2
d = n1/n2
di = n1//n2
e = n1 ** n2

print(f'A soma é {s}, o produto é {m} e a divisão é {(n1/n2):.3f}', end = '')
print(f'Divisão inteira é {di} e potência é {e}')

#se quero a divisão com um número limitado de casas, coloco :.3f (quer dizer que o número float terá apenas 3 números após a virgula)

#Para juntar as duas linhas de print, colocamos no fim do print ent = ''

#Para quebrar a linha no print, colocamos \n para que a linha pule.