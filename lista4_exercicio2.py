def exibirMatriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print(f'[{matriz[i][j]:^5}]', end='')
        print()

def criarMatrizTransposta(matriz):
    matriz_transposta = []
    for j in range(len(matriz[0])):
        matriz_transposta.append([])
        for i in range(len(matriz)):
            result = matriz[i][j]
            matriz_transposta[j].append(result)
    return matriz_transposta

def multiplicarMatrizNumeroReal(numero_real, matriz):
    matriz_multiplicacao = []
    for i in range(len(matriz)):
        matriz_multiplicacao.append([])
        for j in range(len(matriz[0])):
            multiplicacao = numero_real * matriz[i][j] 
            matriz_multiplicacao[i].append(multiplicacao)
    return matriz_multiplicacao

def multiplicarMatrizes(matriz1, matriz2):
    if len(matriz1[0]) != len(matriz2):
        print('\nDimensões incorretas. O número de colunas da matriz A precisa ser igual ao número de linhas da matriz B')
        return
    else:
        matrizes_multiplicacao = [] #Cria a matriz
        for i in range(len(matriz1)):
            matrizes_multiplicacao.append([]) #Adiciona uma linha
            for j in range(len(matriz2[0])):
                matrizes_multiplicacao[i].append(0) #Preenche a linha com o elemento 0
                for k in range(len(matriz1[0])):
                    matrizes_multiplicacao[i][j] += matriz1[i][k] * matriz2[k][j]
        return matrizes_multiplicacao

def criarMatrizReduzida(matriz):
    matriz_reduzida = []
    for _ in range(len(matriz) - 1):
        linha = []
        for _ in range(len(matriz[0]) - 1):
            linha.append(0)
        matriz_reduzida.append(linha)
    return matriz_reduzida

def calcularDeterminante(matriz):
    ordem = len(matriz)
    if(ordem == 1):
        determinante = matriz[0][0]
        return determinante
    elif (ordem == 2):
        principal = matriz[0][0] * matriz[1][1]
        secundaria = matriz[0][1] * matriz[1][0]
        determinante = principal - secundaria
        return determinante
    elif (ordem == 3):
        principal = ((matriz[0][0] * matriz[1][1] * matriz[2][2]) +  (matriz[0][1] * matriz[1][2] * matriz[2][0]) + (matriz[0][2] * matriz[1][0] * matriz[2][1]))
        secundaria = ((matriz[0][2] * matriz[1][1] * matriz[2][0]) + (matriz[0][0] * matriz[1][2] * matriz[2][1]) + (matriz[0][1] * matriz[1][0] * matriz[2][2]))
        determinante = principal - secundaria
        return determinante  
    else:
        determinante = 0
        matriz_reduzida = criarMatrizReduzida(matriz)
        for i in range(len(matriz)):
            linha = 0
            for j in range(len(matriz[0])):
                coluna = 0
                for k in range(len(matriz[0])):
                    if(0 != j and i != k):
                        matriz_reduzida[linha][coluna] = matriz[j][k]
                        coluna += 1
                if(0 != j):
                    linha += 1
                else:
                    linha += 0
            determinante += ((-1) ** (0 + i) * calcularDeterminante(matriz_reduzida)) * matriz[0][i]
        return determinante

def calcularMatrizInversa(matriz):
    ordem = len(matriz)
    matriz_inversa = []
    if (ordem == 1):            
        matriz_inversa = 1 / matriz[0][0]
        return matriz_inversa
    else:
        for linha_elemento in range(len(matriz)):
            matriz_linha = []              
            for coluna_elemento in range(len(matriz[0])):
                matriz_reduzida = criarMatrizReduzida(matriz)
                cofator = 0
                linha = 0
                for j in range(len(matriz[0])):
                    coluna = 0
                    for k in range(len(matriz[0])):
                        if(linha_elemento != j and coluna_elemento != k):
                            matriz_reduzida[linha][coluna] = matriz[j][k]
                            coluna += 1
                    if(linha_elemento != j):
                        linha += 1
                    else:
                        linha += 0
                cofator += (-1) ** (linha_elemento + coluna_elemento) * calcularDeterminante(matriz_reduzida)
                matriz_linha.append(cofator)
            matriz_inversa.append(matriz_linha)
        matriz_inversa = criarMatrizTransposta(matriz_inversa)
        matriz_inversa = multiplicarMatrizNumeroReal(1/calcularDeterminante(matriz), matriz_inversa)
        return matriz_inversa         

def criarMatriz(qtd_linhas, qtd_colunas):
    matriz = []
    for i in range(qtd_linhas):
        linha = []
        for j in range(qtd_colunas):
            elemento = int(input(f'Insira o elemento [{i + 1}] [{j + 1}]: '))
            linha.append(elemento)
        matriz.append(linha)
    return matriz

def metodo_da_matriz_inversa():
    print('\nInforme a matriz de coeficientes: ')
    qtd_linhas_coef = int(input('\nInforme a quantidade de linhas: '))
    qtd_colunas_coef = int(input('Informe a quantidade de colunas: '))

    if not (qtd_linhas_coef > 0 and qtd_colunas_coef > 0):
        print('\nQuantidade de linhas e/ou colunas inválidas')
    else:
        print('')
        matriz_coeficientes = criarMatriz(qtd_linhas_coef, qtd_colunas_coef)
        print('')
        exibirMatriz(matriz_coeficientes)

        if len(matriz_coeficientes) != len(matriz_coeficientes[0]):
            print('\nNão é possível calcular o determinante. A matriz deve ser quadrada')
        elif calcularDeterminante(matriz_coeficientes) == 0:
            print('\nO determinante desta matriz será zero, então a matriz não é invertível')
            print('\nSistema possível indeterminado (SPI) ou Sistema impossível (SI)')
        else:
            print('\nInforme a matriz dos termos independentes: ')
            qtd_linhas_term = len(matriz_coeficientes)
            qtd_colunas_term = 1

            print('')
            matriz_termos = criarMatriz(qtd_linhas_term, qtd_colunas_term)
            print('')
            exibirMatriz(matriz_termos)

            print('\nMatriz inversa: \n')
            matriz_inversa_coef = calcularMatrizInversa(matriz_coeficientes)
            exibirMatriz(matriz_inversa_coef)

            print('\nIncógnitas: \n')
            matriz_incognitas = multiplicarMatrizes(matriz_inversa_coef, matriz_termos)

            incognita = 1
            for i in range(len(matriz_incognitas)):
                for j in range(len(matriz_incognitas[0])):
                    print(f'x{incognita} = {round(matriz_incognitas[i][j], 2)}')
                    incognita += 1
            
            print('\nSistema possível determinado (SPD)')

    return

metodo_da_matriz_inversa()