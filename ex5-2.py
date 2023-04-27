num1 = int(input('Informe um número:'))
num2 = int(input('Informe um número:'))
num3 = int(input('Informe um número:'))

if num3 < num1 and num3 < num2:
    menor = num3
elif num2 < num1 and num2 < num3:
    menor = num2
else:
    menor = num1

print(f'O menor valor é {menor}.')
if menor % 2 == 0:
    print('Ele é par!')
else:
    print('Ele é impar!')