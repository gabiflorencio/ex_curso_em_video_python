#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

cidade = str(input('Digite o nome de uma cidade: '))

maior = cidade.upper().split()
tem = 'SANTO' in maior

print(f'O nome da cidade começa com a palavra SANTO? {tem} ')