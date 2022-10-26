#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro cusa R$60 por dia e R$0,15 por Km rodado.

km = float(input('Km percorridos: '))
dias = int(input('Quantidade de dias de aluguel: '))

total = (0.15 * km) + (60 * dias)

print(f'Com {dias} dias de aluguel e {km} Km rodados, o aluguel custou: R${total}')