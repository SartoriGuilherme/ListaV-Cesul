num1 = int(input('Informe um número:'))
num2 = int(input('Informe um número:'))
num3 = int(input('Informe um número:'))

if num1 > num2 and num1 > num3:
    print(f'O primeiro número é o maior.')
elif num2 > num1 and num2 > num3:
    print(f'O segundo número é o maior.')
elif num3 > num1 and num3 > num2:
    print(f'O terceiro número é o maior.')
elif num1 == num2 and (num1 == num3 or num2 == num3):
    print(f'Os três números são iguais.')
else:
    print(f'Dois dos números são iguais.')