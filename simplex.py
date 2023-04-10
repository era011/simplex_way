# симплекс для max
from print2 import print2
from values import *
from bazis import bazis
from functions import *
# from M_num import M

class simplex:
    def __init__(self,func1:list,usl1:list):    #,dimension,m1):
        self.n=len(func1)
        self.m=len(usl1)
        self.func=[]
        self.usl=[]
        self.bi=[]
        self.znaki=[]
        self.resh=0
        mas=[]
        for i in range(self.n):
            self.func.append(value(float(func1[i]),i))
        for i in range(self.m):
            for j in range(self.n+1):
                if type(usl1[i][j])!=str:
                    mas.append(value(float(usl1[i][j]),j))
                else:
                    self.znaki.append(usl1[i][j]);    
            self.usl.append(mas.copy())
            mas.clear() 
        for i in range(self.m):
            self.bi.append(value(float(usl1[i][-1]),-1))


        # if (self.m<=self.n):
        ci=[]
        self.bp=[]
        zj=[]
        dj=[]
    # Вычисляем
        M_or_no=bazis(self.usl,self.znaki,self.func)       
        print(self.func)         
        print2(self.usl)
        print(f'bi = {self.bi}')
        bazis_per(self.func,self.usl,ci,self.bp)
        print(f'ci = {ci}')
        s=M(0,0)
        for i in range(len(self.usl[0])):
            for j in range(len(self.usl)): 
                # s2=M(self.usl[j][i].get_const(),0)
                s2=self.usl[j][i].c
                # print(s2)
                # print(s2,ci[j],ci[j]*s2)
                s=s+ci[j]*s2
                # print(s)
            zj.append(s)
            s=M(0,0) 
        print(f"zj = {zj}")  
        
        for i in range(len(zj)):
            # print(type(func[i]))
            if type(self.func[i])!=value1:
                dj.append(M(self.func[i].get_const(),0)-zj[i])
            else:
                dj.append(self.func[i].get_m()-zj[i])    
        print(f"dj = {dj}")
        

    # Находим разрешающий столбец
        while (ocenka(dj)>=0):
            print("============================================================================================================")
            
            r=ocenka(dj)
            # print(f'r={r}')
            # if not ogr(r,zj,self.usl):
            #     self.resh=False
            #     break

            zj.clear() 
            dj.clear()
            if r>=0: print(f"r = {r+1}")
            else: print(f"Решено, self.bp = {self.bp}") 
        # Находим разрешающую строку
            br1=[]
            for i in range(len(self.usl)):
                l=self.bi[i]/self.usl[i][r]
                br1.append(l)
            print(f"br1 = {br1}") 
            s=min(br1)
            if s==-1:
                self.resh=1
                break
            br1.clear()
            print(f"s = {s+1}") 

        # Новые базисные перемнные
            for i in range(len(self.usl[s])): self.usl[s][i].baz=False
            self.usl[s][r].baz=True
            self.bp[s]=self.usl[s][r].get_per()
            # print(f"self.bp = {self.bp}")

        # Новые коефициенты базисных переменных    
            ci.clear()
            for i in self.bp:
                for j in self.func:
                    if i==j.get_per():
                        if type(j)==value1:
                            ci.append(j.get_m()) 
                        else: ci.append(M(j.get_const(),0))
            print(f"ci = {ci}")            

        # Преобразуем разрешающую строку 
            mod=value(self.usl[s][r].get_const(),self.usl[s][r].get_index())
            for i in range(len(self.usl[s])):
                if self.usl[s][i].baz:
                    self.usl[s][i]=self.usl[s][i]/mod
                    self.usl[s][i].baz=True
                else:    
                    self.usl[s][i]=self.usl[s][i]/mod
            self.bi[s]=self.bi[s]/mod           

        # Находим делители
            k=[]      
            for i in range(len(self.usl)):
                k.append(self.usl[i][r]/self.usl[s][r])
            # print(f"k = {k}")
            for i in range(len(self.usl[0])):
                for j in range(len(self.usl)):
                    if j!=s:
                        if self.usl[j][i].baz:
                            self.usl[j][i]=self.usl[j][i]-self.usl[s][i]*k[j]
                            self.usl[j][i].baz=True
                        else: self.usl[j][i]=self.usl[j][i]-self.usl[s][i]*k[j]
            for i in range(len(self.bi)):
                if i!=s:
                    self.bi[i]=self.bi[i]-self.bi[s]*k[i]
            k.clear()         
                    
            print(f"func = {self.func}")               
            print2(self.usl) 
            print(f"bi = {self.bi}")

            x=M(0,0)
            for i in range(len(self.usl[0])):
                for j in range(len(self.usl)):
                    if type(ci[j])!=M:
                        x=x+M(ci[j].b(),0)*M(self.usl[j][i].get_const(),0)
                    else:
                        x=x+ci[j]*M(self.usl[j][i].get_const(),0)    
                zj.append(x)
                x=M(0,0)
                s=M(0,0) 
            print(f"zj = {zj}")  
            
            for i in range(len(zj)):
                if type(self.func[i])!=value1:
                    dj.append(M(self.func[i].get_const(),0)-zj[i])
                else:
                    dj.append(self.func[i].get_m()-zj[i])    
            print(f"dj = {dj}") 
            print(f'r={ocenka(dj)}')
        for i in ci:
            if type(i)==M:
                if i.b()!=0:
                    print('asdasd')
                    self.resh=2
                    
        if self.resh==0:
            count=0
            for i in dj:
                if i.b()==0 and i.c1==0:
                    count+=1
            # print(f'asdasdasd {count}')        
            if count>self.m:
                self.resh=1                        
        print("=============================================================================")
        print("=============================================================================")
        for i in range(len(self.bi)):
            self.bi[i]=float(self.bi[i].c)
        self.result=dict(zip(self.bp,self.bi)) 
        # for i in range
    def get_result(self):
        if self.resh==0:
            d={}
            for i in range(self.n):
                per="X"+str(i+1)
                if per in self.result:
                    # d[per]=round((self.result[per]).c,3)
                    d[per]=self.result[per]
                else:
                    d[per]=0
            return d
        elif self.resh==1:
            return 'Бексонечно много решений'
        else:
            return 'Границы несовместимы'




# func=[-1,2,-1,-1]
# usl=[
#     [-1,1,1,0,'=',2]
#     ,[1,1,0,1,'=',4]
# ]
#(1,2,0,0)


# func=[1,4,-10]
# usl=[
#     [2,3,4,'=',18]
#     ,[3,9,1,'=',54]
# ]
# (0,6,0)

# func=[1,-1]
# usl=[
#     [-1,2,'<=',4]
#     ,[3,2,'<=',14]
# ]
# (4.6,0)

# func=[1,-1]
# usl=[
#     [-1,2,'>=',4]
#     ,[3,2,'<=',14]
# ]
# (2.5,3.25)

# func=[1,-1]
# usl=[
#     [-1,2,'>=',4]
#     ,[3,2,'>=',14]
# ]
# бесконечно мног решений

# func=[1,-1]
# usl=[
#     [-4,2,'>=',16]
#     ,[3,2,'<=',14]
# ]
# ограничение исходной задачи несовместны

# func=[-2,4]
# usl=[
#     [-1,2,'<=',4]
#     ,[3,2,'<=',14]
# ]
# бесконечно мног решений

# func=[-3,-4,0,0]
# usl=[
#     [6,6,1,0,'=',36]
#     ,[4,8,0,1,'=',32]
# ]
# (0,0,36,32)

# func=[3,-4]
# usl=[
#     [6,6,'<=',36]
#     ,[4,8,'<=',32]
# ]
# (6,0)

# func=[2,-14]
# usl=[
#     [1,2,'<=',16]
#     ,[5,2,'<=',40]
# ]
# (8,0)

# func=[1,1,0]
# usl=[
#     [2,1,1,'=',16]
#     ,[1,-1,0,'<=',2]
# ]
# (0,16,0)

# func=[150,35]
# usl=[
#     [150,200,'>=',200]
#     ,[14,4,'<=',4]
# ]
# (0,1)
# не совместимы

# func=[1,-3]
# usl=[
#     [3,-2,'<=',3]
#     ,[-5,-4,'<=',-9]
#     ,[2,1,'<=',-5]
# ]
# не имеет решения
# (1,0)

# func=[10,1]
# usl=[
#     [2,11,'<=',33]
#     ,[1,1,'=',7]
#     ,[4,-5,'>=',5]
# ]
# (7,0)

# func=[35,50]
# usl=[
#     [200,150,'>=',200]
#     ,[14,4,'<=',14]
# ]

# func=[-3,12]
# usl=[
#     [1,4,'<=',16]
#     ,[1,-1,'>=',2]
#     ,[3,-5,'<=',8]
# ]
# (4.8,2.8)

# func=[3,-1]
# usl=[
#     [3,-2,'<=',3]
#     ,[-5,-4,'>=',10]
#     ,[2,1,'<=',5]
# ]
# границы несовместимы

# func=[1,2,-1,1]
# usl=[
#     [1,2,0,1,'=',4]
#     ,[1,1,1,0,'=',8]
# ]
# (4,0,4,0)

# func=[-1,2,-1,1]
# usl=[
#     [-1,0,2,1,'=',5]
#     ,[1,1,-1,0,'=',4]
# ]
# (0,4,0,5)

# func=[4,3,-1,-1]
# usl=[
#     [1,2,1,0,'=',8]
#     ,[0,1,2,1,'=',6]
# ]
# (8,0,0,6)

# func=[1,-2,2,-1]
# usl=[
#     [1,0,1,-3,'=',3]
#     ,[2,1,0,1,'=',8]
# ]
# (0,0,29.77,8.9)

# func=[-3,2]
# usl=[
#     [-2,3,'>=',6]
#     ,[1,4,'<=',16]
# ]
# (0,4)




# sim=simplex(func,usl)

# print(sim.get_result())

# a=3.14
# b=int(3.14)

# print(a-b)


