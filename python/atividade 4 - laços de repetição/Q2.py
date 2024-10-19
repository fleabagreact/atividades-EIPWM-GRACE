# Somatória dos números entre x e y
x = int(input("Digite o valor de x (positivo): "))
y = int(input("Digite o valor de y (maior que x): "))

if y > x:
    soma = sum(range(x, y + 1))
    print(f"A soma dos números entre {x} e {y} é: {soma}")
else:
    print("Erro: y deve ser maior que x.")
