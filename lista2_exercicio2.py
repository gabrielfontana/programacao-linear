def exibirMatriz(matriz):
    for linha in matriz:
        print(linha)
    
def somarMatrizes(matriz1, matriz2):
    matriz_soma = []
    for i in range(len(matriz1)):
        matriz_soma.append([])
        for j in range(len(matriz1[0])):
            soma = matriz1[i][j] + matriz2[i][j]
            matriz_soma[i].append(soma)
    return matriz_soma

def multiplicarMatrizNumeroReal(numero_real, matriz):
    matriz_multiplicacao = []
    for i in range(len(matriz)):
        matriz_multiplicacao.append([])
        for j in range(len(matriz[0])):
            multiplicacao = numero_real * matriz[i][j] 
            matriz_multiplicacao[i].append(multiplicacao)
    return matriz_multiplicacao

def criarMatrizTransposta(matriz):
    matriz_transposta = []
    for j in range(len(matriz[0])):
        matriz_transposta.append([])
        for i in range(len(matriz)):
            result = matriz[i][j]
            matriz_transposta[j].append(result)
    return matriz_transposta

def acharDeterminanteOrdem3(matriz):
    principal = ((matriz[0][0] * matriz[1][1] * matriz[2][2]) +  (matriz[0][1] * matriz[1][2] * matriz[2][0]) + (matriz[0][2] * matriz[1][0] * matriz[2][1]))
    secundaria = ((matriz[0][2] * matriz[1][1] * matriz[2][0]) + (matriz[0][0] * matriz[1][2] * matriz[2][1]) + (matriz[0][1] * matriz[1][0] * matriz[2][2]))
    determinante = principal - secundaria
    return determinante

matriz_a = [[1, -1, 0], [2, 3, 4], [0, 1, -2]]
matriz_b = [[2, 7, 2], [8, -1, -3], [-1, 9, 5]]

det_a = acharDeterminanteOrdem3(matriz_a)
result = multiplicarMatrizNumeroReal(det_a, somarMatrizes(matriz_b, criarMatrizTransposta(matriz_a)))
print('Resultado: \n')
exibirMatriz(result)