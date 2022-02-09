def exibirMatriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print(f'[{matriz[i][j]:^5}]', end='')
        print()

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
    if ordem == 1:
        determinante = matriz[0][0]
        return determinante
    elif ordem == 2:
        principal = matriz[0][0] * matriz[1][1]
        secundaria = matriz[0][1] * matriz[1][0]
        determinante = principal - secundaria
        return determinante
    elif ordem == 3:
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
                    if 0 != j and i != k:
                        matriz_reduzida[linha][coluna] = matriz[j][k]
                        coluna += 1
                if 0 != j:
                    linha += 1
                else:
                    linha += 0
            determinante += ((-1) ** (0 + i) * calcularDeterminante(matriz_reduzida)) * matriz[0][i]
        return determinante

def criarMatriz(qtd_linhas, qtd_colunas):
    matriz = []
    for i in range(qtd_linhas):
        linha = []
        for j in range(qtd_colunas):
            elemento = int(input(f'Insira o elemento [{i + 1}] [{j + 1}]: '))
            linha.append(elemento)
        matriz.append(linha)
    return matriz

def MatrizDi(matriz_coeficientes, matriz_termos, coluna):
    matriz_di = []
    for i in range(len(matriz_coeficientes)):
        linha = []
        for j in range(len(matriz_coeficientes[0])):
            if j == coluna:
                elemento = matriz_termos[i][0]
            else:
                elemento = matriz_coeficientes[i][j]
            linha.append(elemento)
        matriz_di.append(linha)
    return matriz_di

def cramer():
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
        else:
            print('\nInforme a matriz dos termos independentes: ')
            qtd_linhas_term = len(matriz_coeficientes)
            qtd_colunas_term = 1

            print('')
            matriz_termos = criarMatriz(qtd_linhas_term, qtd_colunas_term)
            print('')
            exibirMatriz(matriz_termos)

            D = calcularDeterminante(matriz_coeficientes)
            print(f'\nD = {D}\n') 

            lista_det_Di = []
            for i in range(len(matriz_coeficientes[0])):
                index = i
                
                Di = MatrizDi(matriz_coeficientes, matriz_termos, index)
                det_Di = calcularDeterminante(Di)
                lista_det_Di.append(det_Di)

                print(f'Dx{i + 1} = {det_Di}')

                if D != 0:
                    print(f'X{i + 1} = {det_Di}/{D} = {det_Di / D}')
                print('')

            print('Classificação:')
            if D != 0:
                print('\nSistema possível determinado (SPD)')
            else:
                if all(elemento == 0 for elemento in lista_det_Di):
                    print('\nSistema possível indeterminado (SPI)')
                else:
                    print('\nSistema impossível (SI)')                
            
    return

cramer()



