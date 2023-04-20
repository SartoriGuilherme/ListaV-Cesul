num1 = int(input('Informe um valor: '))
num2 = int(input('Informe um valor: '))

if num1 > num2:
    x = num1 - num2
else:
    x = num2 - num1
print(f'A diferença entre o maior e o menor é de {x:.0f}')
