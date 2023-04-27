num1 = int(input('Informe um número:'))
num2 = int(input('Informe um número:'))
num3 = int(input('Informe um número:'))

if num3 < num1 and num3 < num2:
    print('O terceiro número é o menor.')

    if num3 % 2 == 0:
        print(f'{num3} É par.')
    else:
        print(f'Não é par')

elif num2 < num1 and num2 < num3:
    print(f'O segundo número é o menor.')
    if num2 % 2 == 0:
        print(f'{num2} é par.')
    else:
        print(f'Não é par')

else:
    print(f'O primeiro número é o menor.')
    if num1 % 2 == 0:
        print(f'{num1} é par.')
    else:
        print(f'Não é par')
