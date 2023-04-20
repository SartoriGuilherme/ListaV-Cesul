ano = int(input('Informe o ano: '))

if ano % 4 == 0 and (ano % 400 == 0 or ano % 100 != 0):
    print(f'{ano:.0f} é um ano bissexto')
else:
    print(f'{ano:.0f} não é um ano bissexto')