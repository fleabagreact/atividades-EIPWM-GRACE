nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media >= 6.0:
    print(f"Aluno(a) aprovado(a) com média {media:.2f}")
else:
    print(f"Aluno(a) reprovado(a) com média {media:.2f}")
