from math import exp
import p2_task1;
import p2_task2;
import derivative;
import gausslegendre;
import richardson;
import rkn;

# TASK 1 

def task1(icod, params, x, tolm):
    # f = lambda vars: 2*vars[1]**2 + vars[0]**2 + 6*vars[2]**2 -1.0
    # g = lambda vars: 8*vars[1]**3 + 6*vars[1]*vars[0]**2 + 36*vars[1]*vars[0]*vars[2] + 108*vars[1]*vars[2]**2 - params[0]
    # h = lambda vars: 60*vars[1]**4 + (60*vars[1]**2)*(vars[0]**2) + (576*vars[1]**2)*vars[0]*vars[2] + \
    #     (2232*vars[1]**2)*(vars[2]**2) + (252*vars[2]**2)*vars[0]**2 + (1296*vars[2]**3)*vars[0] + \
    #     3348*vars[2]**4 + (24*vars[0]**3)*vars[2] + 3*vars[0] - params[1]
    # s = [f,g,h]
    f = lambda vars: vars[0] - vars[1] + 2 
    g = lambda vars: exp(vars[0]) + 2*vars[1] - 6
    s=[f,g]
    # f = lambda vars: vars[0]+2*vars[1]-2
    # g = lambda vars: vars[0]**2 + 4*vars[1]**2 -4
    # s=[f,g]

    if icod == 1:
        return p2_task1.newton(s,x,tolm,100)
    elif icod == 2:
        return p2_task1.broyden(s,x,tolm,100)
print('Task 1: \n')
for i in range(1,3,1):
    print('ICOD = %i' %i)
    print(task1(i,[2,9.7],[1,1],0.0001))
    # print(task1(i,[0.75,6.5],[1,0,0],0.0001))
    # print(task1(i,[0.00,11.667],[1,0,0],0.0001))

print('+-----+----------------------+---------------------+-----------------------+\n')

# print('Task 2: \n')
# def task2(icod, params, tolm=0,a=0,b=0,delta_x=0,opcao_der=0, n=0, delta1 = 0, delta2 = 0):
#     f = lambda vars,x: vars[0]*exp(vars[1]*x) + vars[2]*x**vars[3]

#     if icod == 1:
#         return p2_task2.bissection(a,b,tolm,f,params)
#     elif icod == 2:
#         return gausslegendre.gausslegendre(a, b, n, params)
#     elif icod == 3: 
#         return derivative.first_order(f,a,delta_x,opcao_der,True,params)
#     elif icod == 4:
#         return richardson.richardson(params,delta1,delta2,a)

# params = [0.25, 0.9, -3.0, 1.2]
# print('icod = 1:')
# print(task2(1,params,0.01, a=1,b=5))
# print('icod = 2:')
# print(task2(2,params, a=1,b=5,n=7))
# print('icod = 3:')
# for i in range(3):
#     if i == 0:
#         print('derivada por passo a frente')
#     elif i == 1:
#          print('derivada por passo atrás')
#     else: 
#          print('derivada por diferença central')
#     print(task2(3,params, a=2, delta_x=0.1, opcao_der=i))
# print('icod = 4:')
# print(task2(4,params, a=2, delta1 = 0.0100001, delta2 = 0.0100000))

# print('+-----+----------------------+---------------------+-----------------------+\n')

# def task3(h, temp, params):
#     return rkn.rkn(h, temp, params)
# print('Task 3: \n')
# print(task3(0.1, 100, [1.0,-2.0,1.5,0.2,1.0,2.0,1,0.1,1.5]))
# print('+-----+----------------------+---------------------+-----------------------+\n')

