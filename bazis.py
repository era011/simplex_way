
from print2 import print2
from values import *

def bazis(usl,znaki,func):
    prov=False
    bazises=[]
    j1=0
    i1=0
    k1=0
    k=0
#Добавляем перемные чтоб привести к каноническому виду
    for i in range(len(usl)):
        if znaki[i]=="<=":
            for s in range(len(usl)):
                if (s==k1) and (i==k1):
                    usl[i].append(value(1,len(usl[i])))
                    usl[i][len(usl[i])-1].baz=True
                    k1=k1+1
                else:  usl[i].append(value(0,len(usl[i])))     
        else:
            for s in range(len(usl)):
                if (s==k1) and (i==k1):
                    usl[i].append(value(-1,len(usl[i])))
                    k1=k1+1
                else:  usl[i].append(value(0,len(usl[i])))   
    
    for i in range(len(usl)):
        func.append(value1(0,0,len(func)+1))
    
    
    prov=False 
                         
 #проверяем на базисность
    m=len(usl)
    n=len(usl[0])
    prov=False
    for i in range(m):
        for j in range(n):
            if usl[i][j].baz==True:
                prov=True
        if prov:
            pass
        else: bazises.append(i)
        prov=False 
 
# Добаляем исскусвенные перемнные
    k1=0
    s=0
    for i in bazises:
        for k in range(s):
            usl[i].append(value(0,len(usl[i])))
        s=s+1
        usl[i].append(value(1,len(usl[i])))
        usl[i][len(usl[i])-1].baz=True
        for k in range(len(bazises)-s):
            usl[i].append(value(0,len(usl[i])))
    for i in range(len(usl)):
        if not (i in bazises):
            for k in range(len(bazises)):
                usl[i].append(value(0,len(usl[i])))
#Добаляем исскуственные переменны в целевую функцию
    s=len(bazises)
    # print(f"bazises = {bazises}, {s}")
    s1=0
    print(len(func),s)
    for i in range(s):
        func.append(value1(0,-1,len(func)-s1+1))
    if s==0 : return False
    else: return True     