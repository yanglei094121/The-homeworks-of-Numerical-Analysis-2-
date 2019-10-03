 #exp(x)在[0，4]的n阶多项式插值及误差
import math
import numpy as np
import matplotlib.pyplot as plt

def truev(x): 
    a=np.exp(x)
    return a

#计算n+1个真值
def truex(x0,xn,n):
    v = np.zeros((n+1,2))#开辟一个数组存x以及对应的y值
    h = (xn-x0)/n#步长
    for i in range(n+1):
        v[i][0]= x0+(h * i)
        v[i][1]=truev(v[i][0])
    return v;

def truearrayx(x0,xn):
    h=0.001;
    o=int((xn-x0)/h)
    m = np.zeros((o,2))
    s = np.zeros(o)
    z = np.zeros(o)
    #print(m);#开辟一个数组存x以及对应的y值
    for i in range(o):
        s[i]= x0+(h * i)
            #print(x[i])
        z[i]=truev(s[i]) 
    return s,z

def Lagrangev(x0,xn,arr,n,t):#输入值：存放真值的数组、插值次数；输出值：函数结果
    p=0
    l=np.zeros(n+1)
    d=np.zeros(n+1)
    if (((t-x0)*n)%(xn-x0)==0 ):#取端点值得真值
        t=int(((t-x0)*n)/(xn-x0))
        print(t)
        p=arr[t][1]
    else:
        for j in range(n+1):
            l[j]=arr[j][1]
            for k in range(n+1):
                if(arr[j][0]-arr[k][0]==0):
                    d[k]=1
                    l[j]=l[j]
                else:
                    d[k]=arr[j][0]-arr[k][0]
                    l[j]=l[j]*(t-arr[k][0])/(d[k])
        for j in range(n+1):
            p=p+l[j]#求和
    return p



def lagrangarrayx(x0,xn,arr,n):
    g = np.zeros(n+1)
    f = np.zeros(n+1)
    h=(xn-x0)/n
    for i in range(n+1):
        g[i]= x0+(h * i)
        f[i]=Lagrangev(x0,xn,arr,n,g[i])
    return g,f


def errorx(x0,xn,n,x):#输入起始值；终值；插值次数；x值
    b=truex(x0,xn,n)
    a=Lagrangev(x0,xn,b,n,x)
    c=truev(x)
    errorv=a-c
    return errorv


#画图：误差曲线;问题，x应该取何值？将x轴离散化求值，而且要把error为0的点避开
def errorarrayx(x0,xn,n):
    h=(xn-x0)/n
    u = np.zeros(n+1)
    r = np.zeros(n+1)
    for i in range(n+1):
        u[i]= x0+(h * i)
        r[i]=errorx(x0,xn,n+1,u[i])
    return u,r

def errorarrayn(x0,xn,x,n):
    #t = np.zeros(n+1)
    ss = np.zeros(n+1)
    for i in range(n+1):
        ss[i]=errorx(x0,xn,i+1,x)
    return ss

x0=0;xn=4;n1=8;n=4;h=(xn-x0)/n
'''
e=truex(x0,xn,n)
e1=truex(x0,xn,n1)
(a,b)=truearrayx(x0,xn)
(c,d)=lagrangarrayx(x0,xn,e,n)
(c1,d1)=lagrangarrayx(x0,xn,e1,n1)
fig = plt.figure(num=1, figsize=(30, 15),dpi=150) 

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False#设置汉语显示
plt.plot(a,b, label='true values', linewidth=4, color='fuchsia')
plt.plot(c,d, label='n=4 Lagrange interpolation', linewidth=3, color='lawngreen', marker='o',
         markerfacecolor='beige', markersize=6)
plt.plot(c1,d1, label='n=8 Lagrange interpolation', linewidth=3, color='cyan', marker='o',
         markerfacecolor='coral', markersize=6)

for x, y in zip(c, d):
    plt.text(x, y, y, ha='center', va='bottom', fontsize=10,rotation=5)
for x1, y1 in zip(c1, d1):
    plt.text(x1, y1, y1, ha='center', va='bottom', fontsize=10,rotation=5)
plt.legend(loc="upper left",fontsize="large")
plt.xlabel("x")
plt.ylabel("Values")

plt.title('Result Of Lagrange Interpolation ',fontsize='xx-large',fontweight='black')
plt.show()
'''
#误差曲线
fig = plt.figure(num=1, figsize=(30, 15),dpi=150)
#(a,b)=errorarrayx(0,4,8)
b=errorarrayn(0,4,3.88,199)#输入n取值的最大值
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False#设置汉语显示
# plt.plot(a,b, label=' error of n=20 Lagrange interpolation',  linewidth=3, color='red', marker='o',
#          markerfacecolor='blue', markersize=6)
# for x, y in zip(a,b):
#     plt.text(x, y, y, ha='center', va='bottom', fontsize=6)
# plt.xlabel("x")
# plt.ylabel("Error")

# plt.title('Error Of Lagrange Interpolation with different x ',fontsize='xx-large',fontweight='black')
plt.plot(range(200),b, label=' error of n=20 Lagrange interpolation',  linewidth=3, color='red', marker='o',
         markerfacecolor='blue', markersize=6)
for x, y in zip(range(200),b):
    plt.text(x, y, y, ha='center', va='bottom', fontsize=6,rotation=10)
plt.xlabel("n")
plt.ylabel("Error")

plt.title('Error Of Lagrange Interpolation with different n ',fontsize='xx-large',fontweight='black')
plt.show()