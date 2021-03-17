#FUNÇÕES
def exibirMatriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print(f'[{matriz[i][j]:^5}]', end='')
        print()

def criarMatriz(qtd_linhas, qtd_colunas):
    matriz = []
    for i in range(qtd_linhas):
        linha = []
        for j in range(qtd_colunas):
            elemento = int(input(f"Insira o elemento [{i + 1}] [{j + 1}]: "))
            linha.append(elemento)
        matriz.append(linha)
    return matriz

def verificarMatriz(matriz):
    if(len(matriz) == len(matriz[0])):
        print('É possível calcular o determinante desta matriz!')
    else:
        print('Não é possível calcular o determinante. A matriz não é quadrada!')

qtd_linhas = int(input('Informe a quantidade de linhas da matriz: '))
qtd_colunas = int(input('Informe a quantidade de colunas da matriz: '))

matriz = criarMatriz(qtd_linhas, qtd_colunas)
exibirMatriz(matriz)
verificarMatriz(matriz)