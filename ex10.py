saldo = float(input('Informe o seu saldo médio:'))

if 0 <= saldo <= 500:
    print(f'Você não tem acesso a nenhum cŕedito.')
elif 501 <= saldo <= 1000:
    credito = saldo * 0.2
    print(f'Você tem acesso a 20% do valor de seu saldo em cŕedito, seu crédito fica de R${credito:.2f}')
elif 1001 <= saldo <= 1600:
    credito = saldo * 0.3
    print(f'Você tem acesso a 30% do valor do seu saldo em crédito, seu crédito fica de R${credito:.2f}')
elif saldo >= 1601:
    credito = saldo * 0.4
    print(f'Você tem acesso a 40% do valor de seu saldo em crédito, seu cŕedito fica de R${credito:.2f}')
else:
    print(f'O saldo médio informado é inválido.')
    