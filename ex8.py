emprego = str(input('Informe a sua função (Testador, Analista de Testes, Programador, Analista de Sistemas, DBA): '))
horastrabalhadas = int(input('Informe o número de horas que trabalha: '))
if emprego == 'Testador':
    valor_hora = 20.0
elif emprego == 'Analista de Testes':
    valor_hora = 35.0
elif emprego == 'Programador':
    valor_hora = 45.0
elif emprego == 'Analista de Sistemas':
    valor_hora = 40.0
elif emprego == 'DBA':
    valor_hora = 50.0
else:
    print('Função não registrada no sistema.')

salario = valor_hora * horastrabalhadas

print(f'O salário é de {salario:.2f} reais.')