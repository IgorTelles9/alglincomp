import math
from prettytable import PrettyTable
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

def func(t,y,yl,params):

    a1,a2,a3,w1,w2,w3,m,c,k = params
    return ((-c*yl)-(k*y)+(a1*math.sin(w1*t))+(a2*math.sin(w2*t))+(a3*math.cos(w3*t)))/m


def rkn(h,temp,params):

    table = PrettyTable(['t', 'x', 'v', 'a'])
    a1,a2,a3,w1,w2,w3,m,c,k = params
    t=0
    y=0
    yl=0
    t_arr = []
    y_arr = []
    yl_arr = []
    func_arr = []
    t_arr.append(t)
    y_arr.append(y)
    yl_arr.append(yl)
    matrix = []
    func_arr.append(func(t,y,yl,params))
    matrix.append([t, y, yl, func(t,y,yl,params)])
    # table.add_row([t, y, yl, func(t,y,yl,params)])
    #print(f't:{t} | x:{y} | v:{yl} | a: {func(t,y,yl,params)}')
    while t < temp:
        k1 = 0.5*h*func(t,y,yl,params)
        q = 0.5*h*(yl+0.5*k1)
        k2 = 0.5*h*func(t+(h/2),y+q,yl+k1,params)
        k3 = 0.5*h*func(t+(h/2),y+q,yl+k2,params)
        l = h*(yl+k3)
        k4 = 0.5*h*func(t+h,y+l,yl+2*k3,params)

        y = y + h*(yl+(1/3)*(k1+k2+k3))
        yl = yl + (1/3)*(k1+2*k2+2*k3+k4)

        t += h
        t = round(t,3)
        table.add_row([t, y, yl, func(t,y,yl,params)])
        t_arr.append(t)
        y_arr.append(y)
        yl_arr.append(yl)
        func_arr.append(func(t,y,yl,params))
        matrix.append([t, y, yl, func(t,y,yl,params)])
        #print(f't:{t } | x:{y} | v:{yl} | a: {func(t,y,yl,params)}')
        

    #print(matrix)
    # t_arr1 = np.array(t_arr)
    # y_arr1 = np.array(y_arr)
    # yl_arr1 = np.array(yl_arr)
    # func_arr1 = np.array(func_arr)

    # df1 = pd.DataFrame(arr)
    # df2 = pd.DataFrame(arr)
    # df3 = pd.DataFrame(arr)

    # x_ticks = np.arange(0,100,0.1)
    # #x_ticks = range(len(t_arr))
    # #plt.plot(x_ticks, t_arr)
    # plt.plot(x_ticks, y_arr)
    # plt.show()
    return y

#print(rkn(0.1, 10, [1,2,1.5,0.05,1,2,1,0.1,2]))
#print(rkn(0.1,10,1,2,1.5,0.05,1,2,1,0.1,2))
