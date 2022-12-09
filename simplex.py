# симплекс для max
from print2 import print2
from values import *
from bazis import bazis
from functions import *
# from M_num import M


print(f"Количество переменных3")
n=int(input())
print("Введите количество условий")
m=int(input())
if (m<=n):
    usl=[[0 for j in range(n) ]for j in range(m)]
    znaki=[]
    bi=[]
    ci=[]
    bp=[]
    zj=[]
    func=[]
    dj=[]
    print("Коефициенты переменных в целевой фукнции")
    for i in range(n):
        print(f"Введите коефициент при переменной x{i+1}")
        func.append(value(int(input()),i))
    for i in range(m):
        for j in range(n):
            print(f"Коефициент при переменной x{j+1} {i+1}-го условия ")
            usl[i][j]=value(int(input()),j)            
    for i in range(m):
        print(f"Введите знак <= или >= {i+1}-го условия") 
        znaki.append(str(input())) 
        print(f"Введите знак константу, стоящее после знака {i+1}-го условия") 

        bi.append(value(int(input()),-1))
    # print(bi)    

# Вычисляем
    M_or_no=bazis(usl,znaki,func)       
    print(func)         
    print2(usl)
    bazis_per(func,usl,ci,bp)
    s=M(0,0)
    for i in range(len(usl[0])):
        for j in range(len(usl)): 
            # print(ci[j])
            s2=M(usl[j][i].get_const(),0)
            s=s+ci[j]*s2  #M(usl[j][i].get_const(),0)   
        zj.append(s)
        s=M(0,0) 
    print(f"zj = {zj}")  
    
    for i in range(len(zj)):
        # print(type(func[i]))
        if type(func[i])!=value1:
            dj.append(M(func[i].get_const(),0)-zj[i])
        else:
            dj.append(func[i].get_m()-zj[i])    
    print(f"dj = {dj}")
    

# Находим разрешающий столбец
    while (ocenka(dj)>=0):
        print("============================================================================================================")
        zj.clear() 
        r=ocenka(dj)
        dj.clear()
        if r>=0: print(f"r = {r+1}")
        else: print(f"Решено, bp = {bp}") 
    # Находим разрешающую строку
        br1=[]
        for i in range(len(usl)):
            l=bi[i]/usl[i][r]
            br1.append(l)
        print(f"br1 = {br1}") 
        s=min(br1)
        br1.clear()
        print(f"s = {s}") 

    # Новые базисные перемнные
        for i in range(len(usl[s])): usl[s][i].baz=False
        usl[s][r].baz=True
        bp[s]=usl[s][r].get_per()
        print(f"bp = {bp}")
    # Новые коефициенты базисных переменных    
        ci.clear()
        for i in bp:
            for j in func:
                if i==j.get_per():
                    if type(j)==value1:
                        ci.append(j.get_m()) 
                    else: ci.append(M(j.get_const(),0))
        print(f"ci = {ci}")            

    # Преобразуем разрешающую строку 
        mod=value(usl[s][r].get_const(),usl[s][r].get_index())
        for i in range(len(usl[s])):
            if usl[s][i].baz:
                usl[s][i]=usl[s][i]/mod
                usl[s][i].baz=True
            else:    
                usl[s][i]=usl[s][i]/mod
        bi[s]=bi[s]/mod           

    # Находим делители
        k=[]      
        for i in range(len(usl)):
            k.append(usl[i][r]/usl[s][r])
        print(f"k = {k}")
        for i in range(len(usl[0])):
            for j in range(len(usl)):
                if j!=s:
                    if usl[j][i].baz:
                        usl[j][i]=usl[j][i]-usl[s][i]*k[j]
                        usl[j][i].baz=True
                    else: usl[j][i]=usl[j][i]-usl[s][i]*k[j]
        for i in range(len(bi)):
            if i!=s:
                 bi[i]=bi[i]-bi[s]*k[i]
        k.clear()         
                
        print(f"func = {func}")               
        print2(usl) 
        print(f"bi = {bi}")

        x=M(0,0)
        for i in range(len(usl[0])):
            for j in range(len(usl)):
                if type(ci[j])!=M:
                    x=x+M(ci[j].b(),0)*M(usl[j][i].get_const(),0)
                else:
                    x=x+ci[j]*M(usl[j][i].get_const(),0)    
            zj.append(x)
            x=M(0,0)
            s=M(0,0) 
        print(f"zj = {zj}")  
        
        for i in range(len(zj)):
            # print(type(func[i]))
            if type(func[i])!=value1:
                dj.append(M(func[i].get_const(),0)-zj[i])
            else:
                dj.append(func[i].get_m()-zj[i])    
        print(f"dj = {dj}") 

    print("=============================================================================")
    print("=============================================================================")
    print("ОПТИМАЛЬНОЕ РЕШЕНИЕ:")
    for i in range(len(bi)):
        print(f"{bp[i]} = {bi[i]}")



