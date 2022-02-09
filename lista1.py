#FUNÇÕES
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

def subtratirMatrizes(matriz1, matriz2):
    matriz_subtracao = []
    for i in range(len(matriz1)):
        matriz_subtracao.append([])
        for j in range(len(matriz1[0])):
            subtracao = matriz1[i][j] - matriz2[i][j]
            matriz_subtracao[i].append(subtracao)
    return matriz_subtracao

def multiplicarMatrizes(matriz1, matriz2):
    matrizes_multiplicacao = [] #Cria a matriz
    for i in range(len(matriz1)):
        matrizes_multiplicacao.append([]) #Adiciona uma linha
        for j in range(len(matriz2[0])):
            matrizes_multiplicacao[i].append(0) #Preenche a linha com o elemento 0
            for k in range(len(matriz1)):
                matrizes_multiplicacao[i][j] += matriz1[i][k] * matriz2[k][j]
    return matrizes_multiplicacao

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

def acharDeterminante(matriz):
    principal = matriz[0][0] * matriz[1][1]
    secundaria = matriz[0][1] * matriz[1][0]
    determinante = principal - secundaria
    return determinante

def criarMatrizInversa(matriz, determinante):
    #1º passo - dividir todos os elementos da matriz pelo determinante
    matriz_inversa = []
    for i in range(len(matriz)):
        matriz_inversa.append([])
        for j in range(len(matriz[0])):
            resultado = matriz[i][j] / determinante
            matriz_inversa[i].append(resultado)
   
    #2º passo - permutar os elementos da diagonal principal
    a = matriz_inversa[0][0]
    b = matriz_inversa[1][1]
    matriz_inversa[0][0] = b
    matriz_inversa[1][1] = a

    #3º passo - inverter o sinal dos elementos da diagonal secundária
    matriz_inversa[0][1] = matriz_inversa[0][1] * (-1)
    matriz_inversa[1][0] = matriz_inversa[1][0] * (-1)

    return matriz_inversa

#MATRIZES
matriz_a = [[2, 1], [-3, 4]]
matriz_b = [[0, -1], [2, 5]]
matriz_c = [[3, 0], [6, 1]]

#RESOLUÇÕES
#1) A * B
exercicio_1 = multiplicarMatrizes(matriz_a, matriz_b)

print('\nExercício 1: ')
exibirMatriz(exercicio_1)

#2) (A + B) + 4 * C
exercicio_2 = somarMatrizes(somarMatrizes(matriz_a, matriz_b), multiplicarMatrizNumeroReal(4, matriz_c))

print('\nExercício 2: ')
exibirMatriz(exercicio_2)

#3) [A + (B + C^t)] * B^(-1)
exercicio_3a = somarMatrizes(matriz_a, subtratirMatrizes(matriz_b, criarMatrizTransposta(matriz_c)))
exercicio_3b = criarMatrizInversa(matriz_b, acharDeterminante(matriz_b))
exercicio_3 = multiplicarMatrizes(exercicio_3a, exercicio_3b)

print('\nExercício 3: ')
exibirMatriz(exercicio_3)

#4) A * A^(-1) = In
exercicio_4 = multiplicarMatrizes(matriz_a, criarMatrizInversa(matriz_a, acharDeterminante(matriz_a)))

print('\nExercício 4: ')
exibirMatriz(exercicio_4)

#5) B + A^t * C^(-1) - B^t
exercicio_5a = multiplicarMatrizes(criarMatrizTransposta(matriz_a), criarMatrizInversa(matriz_c, acharDeterminante(matriz_c)))
exercicio_5b = somarMatrizes(matriz_b, exercicio_5a)
exercicio_5 = subtratirMatrizes(exercicio_5b, criarMatrizTransposta(matriz_b))

print('\nExercício 5: ')
exibirMatriz(exercicio_5)