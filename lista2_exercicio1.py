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

def verificarDeterminanteMatriz(qtd_linhas, qtd_colunas):
    if(qtd_linhas == qtd_colunas):
        return '\nÉ possível calcular o determinante desta matriz!'
    else:
        return '\nNão é possível calcular o determinante'

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
            return 'Ainda não vimos como calcular o determinante de uma matriz dessa ordem'
    else:
        return 'A matriz não é quadrada'

def exibirCalculoDeterminante(matriz):
    return calcularDeterminante(matriz)

qtd_linhas = int(input('\nInforme a quantidade de linhas da matriz: '))
qtd_colunas = int(input('Informe a quantidade de colunas da matriz: '))

print('')
matriz = criarMatriz(qtd_linhas, qtd_colunas)

print('')
exibirMatriz(matriz)

print(verificarDeterminanteMatriz(qtd_linhas, qtd_colunas))
print('->', exibirCalculoDeterminante(matriz))