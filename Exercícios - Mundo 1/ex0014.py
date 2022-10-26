#Faça um conversor de temperatura e que ele converta Cº para Fº e para K

temp = float(input('Digite a temperatura em graus celcius: '))
k = temp + 273
f = (temp * 9/5 ) + 32

print(f'A temperatura em graus celcius é {temp} Cº, em fahrenheit é {f} Fº e em Kelvin é {k} K')