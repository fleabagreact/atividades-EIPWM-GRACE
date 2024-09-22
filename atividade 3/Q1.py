texto = input("Digite qualquer palavra: ")

if len(texto) >= 5:
    print(f"Tem {len(texto)} caracteres")

else:
    print(f"É menor que 5 caracteres. Tem {len(texto)} caracteres")