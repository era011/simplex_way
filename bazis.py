
from print2 import print2
from values import *

def bazis(usl,znaki,func):
    prov=False
    bazises=[]
    j1=0
    i1=0
    k=0
#Добавляем перемные чтоб привести к каноническому виду
    kol=len(usl[0])
    # for i in range(len(usl)):
    #     if znaki[i]!='=':
    #         if znaki[i]=="<=":
    #             for s in range(len(usl)):
    #                 if (s==k1) and (i==k1):
    #                     usl[i].append(value(1,len(usl[i])))
    #                     usl[i][len(usl[i])-1].baz=True
    #                     k1=k1+1
    #                 else:  usl[i].append(value(0,len(usl[i])))     
    #         else:
    #             for s in range(len(usl)):
    #                 if (s==k1) and (i==k1):
    #                     usl[i].append(value(-1,len(usl[i])))
    #                     k1=k1+1
    #                 else:  usl[i].append(value(0,len(usl[i])))                   
    

    for i in range(len(usl)):
        if znaki[i]!='=':
            if znaki[i]=='<=':
                for j in range(len(usl)):
                    if j!=i:
                        usl[j].append(value(0.0,len(usl[i])))   
                usl[i].append(value(1.0,len(usl[i])))
                usl[i][-1].baz=True           
            else:          
                for j in range(len(usl)):
                    if j!=i:
                        usl[j].append(value(0.0,len(usl[i])))
                usl[i].append(value(-1.0,len(usl[i])))
    
    if kol!=len(usl[0]):
        for i in range(kol,len(usl[0])):
            func.append(value1(0,0,len(func)+1))
    
    
    prov=False 
                         
 #проверяем на базисность
    m=len(usl)
    n=len(usl[0])
    prov=False
    prov1=False
    for i in range(m):
        for j in range(n):
            if usl[i][j].baz==True:
                prov=True
        if not prov:
            for j in reversed(range(n)):
                if usl[i][j].c==1:
                    # print(f'sssssssssssssss {usl[i][j]}')
                    for k in range(m):
                        # print(f'sadasdasd {usl[k][j]}')
                        if k!=i:
                            if usl[k][j].c!=0:
                                prov1=True
                                break
                    if not prov1:    
                        prov=True
                        usl[i][j].baz=True      
                        break  
        if prov:
            pass
        else: bazises.append(i)
        prov=False 
 
# Добаляем исскусвенные перемнные
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
    for i in range(s):
        func.append(value1(0,-1,len(func)-s1+1))
    if s==0 : return False
    else: return True     