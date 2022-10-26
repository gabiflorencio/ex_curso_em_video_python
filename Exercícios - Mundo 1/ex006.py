#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = int(input('Digite um número: '))

d = 2*n #dobro
t = 3*n #triplo
r = n**(1/2) #raiz quadrada

print(f'O seu número é {n} \n O dobro é {d} \n O triplo é {t} \n A raiz quadrada é {r:.3f}')

