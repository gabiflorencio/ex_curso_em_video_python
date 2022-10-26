#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
#Considere US$ 1.00 = R$ 3.27

print('------ CALCULADORA DE CONVERSÃO REAL > DOLAR --------')
print('')

n = float(input('Quanto você tem na carteira? '))
d = n/3.27

print('')
print(f'Você pode comprar {d:.2f} dolares.')