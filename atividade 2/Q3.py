valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))

soma = valor1 + valor2

if soma >= 10:
    resultado = soma + 5
else:
    resultado = soma - 7

print(f"O novo resultado é: {resultado:.2f}")