A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))

if A == B:
    print("Os valores são iguais.")
else:
    if A > B:
        diferenca = A - B
    else:
        diferenca = B - A

    print(f"A diferença entre o maior e o menor valor é: {diferenca}")