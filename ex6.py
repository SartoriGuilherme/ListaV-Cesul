lado1 = int(input('Informe o lado 1 do triângulo:'))
lado2 = int(input('Informe o lado 2 do triângulo:'))
lado3 = int(input('Informe o lado 3 do triângulo:'))

if lado1 == lado2 and lado2 == lado3:
    print(f'É um triângulo equilátero.')
elif lado1 != lado2 and lado2 != lado3 and lado3 != lado1:
    print(f'É um triângulo escaleno.')
    if lado1 + lado2 > lado3 or lado3 + lado1 > lado2 or lado2 + lado3 > lado1:
        print(f'Sim, as medidas formam um triângulo.')
elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3 and lado2 != lado1:
    print(f"É um triângulo isoscéles.")
    if lado1 + lado2 > lado3 or lado3 + lado1 > lado2 or lado2 + lado3 > lado1:
        print(f'Sim, as medidas formam um triângulo.')