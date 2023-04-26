nota = float(input("Digite a nota do aluno: "))

if 9.0 <= nota <= 10.0:
    print("Superior")
elif 7.0 <= nota < 9.0:
    print("Médio Superior")
elif 5.0 <= nota < 7.0:
    print("Médio")
elif 3.0 <= nota < 5.0:
    print("Médio Inferior")
elif 0.1 <= nota < 3.0:
    print("Inferior")
elif nota == 0.0:
    print("Sem Rendimento")
else:
    print("Nota inválida. Digite um valor entre 0 e 10.")
