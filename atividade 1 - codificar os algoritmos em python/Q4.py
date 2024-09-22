# Trapézio
base_maior = float(input("Digite o comprimento da base maior do trapézio: "))
base_menor = float(input("Digite o comprimento da base menor do trapézio: "))
altura = float(input("Digite a altura do trapézio: "))

area = (base_maior + base_menor) * altura / 2

print(f"A área do trapézio é: {area:.2f}m²")