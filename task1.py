def displayMetodos():
    print('Decomposicao LU (ICOD=1)')
    print('Decomposicao de Cholesky (ICOD=2)')
    print('Procedimento Iterativo Jacobi (ICOD=3')
    print('Procedimento Iterativo Gauss-Seidel (ICOD=4')

def displayDeterminante():
    print('Nao calcular determinante (IDET = 0)')
    print('Calcular determinante (IDET > 0)')
    


def configura():
    ordem = int(input('Ordem do sistema de equacoes:'))
    icod = int(input('ICOD relativo ao metodo de analise (para exibir novamente a lista de metodos, digite 0):'))
    if icod == 0:
      displayMetodos()
      icod = int(input('ICOD relativo ao metodo de analise:'))
    
    idet = 0
    if icod == 1 or icod == 2:
      displayDeterminante()
      idet = int(input('IDET relativo ao determinante: '))
    else:
      print('o metodo escolhido nao calcula determinante')
    
    arquivo_a = input('Nome do arquivo que contem a matriz A:')
    arquivo_b = input('Nome do arquivo que contem o vetor B:')
    
    tolm = 0
    if icod == 3 or icod == 4:
      tolm = int(input('Tolerancia maxima para solucao iterativa (1 = 10^-1; 2 = 10^-2, etc):'))
    
    return ordem,icod,idet, arquivo_a, arquivo_b, tolm 


print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
print('CALCULADORA DE SISTEMAS LINEARES')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
print('Este programa resolve sistemas lineares utilizando os seguintes métodos:')
displayMetodos()
(ordem, icod, idet, arquivo_a, arquivo_b, tolm) = configura()

print('end')
