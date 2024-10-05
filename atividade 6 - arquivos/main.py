#########
# Função para calcular média entre N números. 
def mediaN (valores):
    quantidade = len(valores)
    soma = 0
    for i in range(quantidade):
        soma += valores[i]
    return soma / quantidade

#########
# Função que realiza a leitura do arquivo de entrada.
def ler_entrada():
    with open("atividade 6 - arquivos/notas.in") as notas:
        dados = notas.readlines()
        for i in range(len(dados)):
            dados[i] = dados[i].rstrip("\n").split()
            for j in range(1, len(dados[i])):
                dados[i][j] = int(dados[i][j])
        return dados

#########
# Função que verifica os alunos aprovados
def verifica_aprovados(notas):
    numero_alunos = len(notas)
    for i in range(numero_alunos):
        nome = notas[i][0]
        media = mediaN(notas[i][1:])
        media = round(media, 1)
        notas[i].append(media)
        if media >= 7.0:
            notas[i].append("Aprovado")
        else:
            notas[i].append("Reprovado")
    return notas

#########
# Função que conta e exporta a quantidade de aprovados e reprovados
def conta_aprovados_reprovados(notas):
    aprovados = 0
    reprovados = 0
    
    for aluno in notas:
        if aluno[-1] == "Aprovado":
            aprovados += 1
        else:
            reprovados += 1

    # Imprimir no terminal
    print(f"Quantidade de alunos aprovados: {aprovados}")
    print(f"Quantidade de alunos reprovados: {reprovados}")

    # Escrever no arquivo resultado2.txt
    with open("atividade 6 - arquivos/resultado2.txt", "w") as arquivo:
        arquivo.write(f"Quantidade de alunos aprovados: {aprovados}\n")
        arquivo.write(f"Quantidade de alunos reprovados: {reprovados}\n")

#########
# Função que escreve no arquivo de saída resultado.txt.
def exporta_resultado(notas):
    with open("atividade 6 - arquivos/resultado.txt", "w") as arquivo:
        numero_alunos = len(notas)
        for i in range(numero_alunos):
            nome = notas[i][0]
            situacao = notas[i][-1]
            arquivo.write(f"O aluno {nome} foi {situacao}\n")

##########################
# O programa começa aqui
notas = ler_entrada()
notas = verifica_aprovados(notas)
exporta_resultado(notas)
conta_aprovados_reprovados(notas)

# Imprimir todas as informações no terminal
for linha in notas:
    print(linha)
