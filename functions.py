from values import *

def bazis_per(func,usl,ci,bp):
    for i in range(len(usl)):
        for j in range(len(usl[0])):
            if usl[i][j].baz:
                bp.append(usl[i][j].get_per())

    print(f"Базисные перемнные {bp}")

    for i in bp:
        for j in func:
            if j.get_per()==i:
                # print(type(j))
                ci.append(j.get_m())  

    # print(f"Коефициенты при базисных элементах в целевой фукнции {ci}")       

def max(list1,max1):
    i1=0
    for i in range(len(list1)):
        if list1[i].proverka()>=max1:
            max1=list1[i].proverka()
            i1=i
    return i1

def ocenka(dj):
    max1=dj[0].get_const()
    r=max(dj,max1)
    if max1>0: return r 
    else: return -1       

def min(list2):
    i1=0
    list1=[]
    list3=[]
    for i in range(len(list2)):
        if list2[i].c>=0: 
            list1.append(list2[i])
            list3.append(i)
    min1=list1[0].c    
    for i in range(len(list1)):
        if list1[i].c<=min1:
            min1=list1[i].c
            i1=list3[i]
    return i1 

def proverka_na_int(str1):
    bool1=False
    list1=['1','2','3','4','5','6','7','8','9']
    for i in str1:
        if i in list1:bool1=True
    return bool1
