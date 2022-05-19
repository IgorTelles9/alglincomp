import determinant
import wr_utils
import eigen
import utils

loop = True

print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-')
print('CALCULADORA DE AUTOVALORES E AUTOVETORES')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-')
print()

print()
print('Este programa calcula autovalores e autovetores utilizando os seguintes métodos:')
print()

wr_utils.displayMethodOptions(2)

while loop:
    (ordem, icod, idet, arquivo_a, tolm) = wr_utils.config(2)

    matriz = wr_utils.getMatrix(arquivo_a)
    det = 0
    itCounter = 0

    while(icod == 2 and not utils.isSymmetric(matriz, ordem)):
        print('ATENCAO!')
        print('O metodo escolhido so funciona para matrizes simetricas.')
        print('A matriz inserida NAO e simetrica.')
        print('Por favor, entre novamente com as informacoes.')
        print()
        (ordem, icod, idet, arquivo_a, tolm) = wr_utils.config(2)
        matriz = wr_utils.getMatrix(arquivo_a)

    # ############### calculo de autovetores e autovalores ####################
    if icod == 1:
        # ############ power method ###############
        autovalor, autovetor, itCounter = eigen.power_method(
            matriz, ordem, tolm)
        # ############ fim power method ###############

    if icod == 2:
        # ############ metodo de jacobi ###############
        (autovalores, autovetores, itCounter) = eigen.jacobi(matriz, ordem, tolm)
        autovalores_list = [autovalores[i][i] for i in range(ordem)]

        # calculo de determinante
        if idet > 0:
            det = determinant.getTriangular(autovalores, ordem)
        # fim calculo de determinante
        # ############ fim metodo de jacobi ###############

    # ############### fim calculo de autovetores e autovalores ####################

    # ############## resultados ##################
    if icod == 1:
        print('Maior autovalor: ')
        print(autovalor)
        print()

        print('Autovetor associado: ')
        print(wr_utils.printVector(autovetor))
        print()

    if icod == 2:
        print('Autovalores: ')
        print(wr_utils.printVector(autovalores_list))
        print()

        print('Matriz de Autovetores: ')
        print(wr_utils.printMatrix(autovetores))
        print()

        if idet > 0:
            print('Determinante:')
            print(det)
            print()

    print('Numero de iteracoes: %s' % (itCounter))
    print()

    with open('task2-saida.txt', 'w') as writer:
        if icod == 1:
            writer.write('Maior autovalor:\n ')
            writer.write(str(autovalor))
            writer.write('\n')

            writer.write('Autovetor associado:\n ')
            writer.write(wr_utils.printVector(autovetor))
            writer.write('\n')

        if icod == 2:
            writer.write('Autovalores:\n ')
            writer.write(wr_utils.printVector(autovalores_list))
            writer.write('\n')

            writer.write('Matriz de Autovetores: \n')
            writer.write(wr_utils.printMatrix(autovetores))
            writer.write('\n')

            if idet > 0:
                writer.write('Determinante:\n')
                writer.write(str(det) + '\n')
                writer.write('\n')

        writer.write('Numero de iteracoes: %s' % (itCounter))
        writer.write('\n')

    # ############## fim resultados ##################

    again = input('Gostaria de realizar outros calculos? (s para sim) ')
    print()
    if again != 's':
        loop = False

print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
