import substitution
import lu
import determinant
import jacobi
import gausseidel
from chule import cholesky
import wr_utils
import utils 
loop = True

print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
print('CALCULADORA DE SISTEMAS LINEARES')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
print()

print()
print('Este programa resolve sistemas lineares utilizando os seguintes métodos:')
print()

wr_utils.displayMethodOptions(1)

while loop:
    (ordem, icod, idet, arquivo_a, arquivo_b, tolm) = wr_utils.config(1)

    matriz = wr_utils.getMatrix(arquivo_a)
    vetor = wr_utils.getMatrix(arquivo_b)
    print(vetor)
    vetor = utils.matrixToVec(vetor)
    print(vetor)
    print()
    x = []
    det = 0
    itCounter = 0
    error = []

    # ############### resolucao do sistema ####################
    # ############ decomposicao LU ###############
    if icod == 1:
        matriz_lu = lu.decomposition(matriz, ordem)
        y = substitution.foward(matriz_lu, vetor, ordem)
        x = substitution.back(matriz_lu, y, ordem)

        # ########### calculo do determinante ###############
        if idet > 0:
            det = determinant.getTriangular(matriz_lu, ordem)
        # ########### fim calculo do determinante ###############

    # ############ fim decomposicao LU ###############

    # ############ metodo de cholesky ###############

    if icod == 2:
        matriz_cholesky, transposta_cholesky, det = cholesky(matriz, ordem, idet)
        y = substitution.foward(matriz_cholesky, vetor, ordem, trueLower=True)
        x = substitution.back(transposta_cholesky, y, ordem)

    # ############ fim do metodo de cholesky ###############

    # ############ metodo de jacobi ###############
    if icod == 3:
        if not jacobi.converge(matriz, ordem):
            print()
            print('ATENCAO:')
            print('A matriz NAO e diagonal dominante.')
            print('Portanto NAO ha garantia de CONVERGENCIA para o metodo de Jacobi.')
            print()

        x, itCounter, error = jacobi.method(matriz, vetor, ordem, tolm)
    # ############ fim metodo de jacobi ###############

    # ############ metodo de gauss-seidel ###############

    if icod == 4:
        if not jacobi.converge(matriz, ordem):
            print()
            print('ATENCAO:')
            print('A matriz NAO e diagonal dominante.')
            print('Portanto NAO ha garantia de CONVERGENCIA para o metodo de Jacobi.')

        x, itCounter, error = gausseidel.seidel(matriz, vetor, ordem, tolm)

    # ############ fim do metodo de gauss-seidel ###############

    # ############### fim resolucao do sistema ####################

    # ############## resultados ##################
    print('Vetor X:')
    print(wr_utils.printVector(x))
    if idet > 0:
        print('Determinante:')
        print(round(det, tolm))
        print()

    if icod == 2:
        print('Matriz da decomposição de Cholesky:')
        print(matriz_cholesky)                                       
        print('Determinante:')
        print(det)

    if icod == 3 or icod == 4:
        print('Numero de iteracoes: %s' % (itCounter))
        print()
        print('Historico da variacao do erro: ')
        print(error)
        print()
        
    with open('task1-saida.txt', 'w') as writer:
        writer.write('Vetor X: \n')
        writer.write(wr_utils.printVector(x) + '\n')
        if idet > 0:
            writer.write('Determinante:\n')
            writer.write(str(round(det, tolm)) + '\n')
        if icod == 3 or icod == 4:
            writer.write('Numero de iteracoes: %s' % (itCounter))
            writer.write('\n')
            writer.write('Historico da variacao do erro:\n ')
            writer.write(str(error))
    # ############## fim resultados ##################

    again = input('Gostaria de resolver outro sistema? (s para sim) ')
    print()
    if again != 's':
        loop = False

print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
