import sys

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
            elemento = int(input(f'Insira o elemento [{i + 1}] [{j + 1}]: '))
            linha.append(elemento)
        matriz.append(linha)
    return matriz

def verificarDeterminanteMatriz(matriz):
    qtd_linhas = len(matriz)
    qtd_colunas = len(matriz[0])
    
    if(qtd_linhas == qtd_colunas):
        print('\nÉ possível calcular o determinante desta matriz!') 
    else:
        print('\nNão é possível calcular o determinante')
        sys.exit()

def criarMatrizReduzida(matriz):
    matriz_reduzida = []
    for _ in range(len(matriz) - 1):
        linha = []
        for _ in range(len(matriz[0]) - 1):
            linha.append(0)
        matriz_reduzida.append(linha)
    return matriz_reduzida

def calcularDeterminante(matriz):
    if(len(matriz) == len(matriz[0])):
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
    else:
        print('\nA matriz não é quadrada')
        sys.exit()

def calcularCofator(matriz):
    if(len(matriz) == len(matriz[0])):
        ordem = len(matriz)

        linha_elemento = int(input('\nInforme a linha do elemento para calcular o cofator: '))
        coluna_elemento = int(input('Informe a coluna do elemento para calcular o cofator: '))

        if not (linha_elemento > 0 and linha_elemento <= len(matriz) and coluna_elemento > 0 and coluna_elemento <= len(matriz[0])):
            print('\níndices de linha ou coluna inválidos')
            sys.exit()
        else:
            if (ordem >= 2):
                linha_elemento -= 1
                coluna_elemento -= 1
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
                print(matriz_reduzida)
                return cofator
            else:
                print('\nNão é possível calcular o cofator')
                sys.exit()
    else:
        print('\nA matriz não é quadrada')
        sys.exit()

def exibirCalculoDeterminante(matriz):
    return calcularDeterminante(matriz)

qtd_linhas = int(input('\nInforme a quantidade de linhas da matriz: '))
qtd_colunas = int(input('Informe a quantidade de colunas da matriz: '))

print('')
matriz = criarMatriz(qtd_linhas, qtd_colunas)

print('')
exibirMatriz(matriz)

verificarDeterminanteMatriz(matriz)

print('\nDeterminante:', exibirCalculoDeterminante(matriz))

print('\nCofator:', calcularCofator(matriz))


