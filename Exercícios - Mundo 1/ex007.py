#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.


print('-----------BEM-VINDOS AO SISTEMA ESCOLAR-------------')
print('')

nome = str(input('Nome do aluno: '))
d = str(input('Disciplina: '))
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2


print(f'O discente {nome}, teve média {m} na disciplina de {d}.')
