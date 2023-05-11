poluicao = float(input('Informe a média de poluição da empresa: '))

if 0.05 <= poluicao <= 0.25:
    print(f'O nível de poluição está aceitável.')
elif 0.25 <= poluicao <= 0.3:
    print(f'As industrias do 1º grupo estão intimadas a suspender suas atividades.')
elif 0.31 <= poluicao <= 0.4:
    print(f'As industrias do 1º e 2º grupo estão intimadas a suspenderem suas atividades.')
elif poluicao > 0.41:
    print(f'Os três grupos devem ser notificados e suspender suas atividades.')