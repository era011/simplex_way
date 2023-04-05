# симплекс для max
from print2 import print2
from values import *
from bazis import bazis
from functions import *
# from M_num import M

class simplex:
    def __init__(self,func1:list,usl1:list,dimension,m1):
        self.n=dimension
        self.m=m1
        self.func=[]
        self.usl=[]
        self.bi=[]
        self.znaki=[]
        mas=[]
        for i in range(dimension):
            self.func.append(value(float(func1[i]),i))
        for i in range(self.m):
            for j in range(dimension+1):
                if type(usl1[i][j])!=str:
                    mas.append(value(float(usl1[i][j]),j))
                else:
                    self.znaki.append(usl1[i][j]);    
            self.usl.append(mas.copy())
            mas.clear() 
        for i in range(self.m):
            self.bi.append(value(float(usl1[i][-1]),-1))


        if (self.m<=self.n):
            ci=[]
            bp=[]
            zj=[]
            dj=[]
        # Вычисляем
            M_or_no=bazis(self.usl,self.znaki,self.func)       
            # print(self.func)         
            # print2(self.usl)
            bazis_per(self.func,self.usl,ci,bp)
            s=M(0,0)
            for i in range(len(self.usl[0])):
                for j in range(len(self.usl)): 
                    s2=M(self.usl[j][i].get_const(),0)
                    s=s+ci[j]*s2 
                zj.append(s)
                s=M(0,0) 
            # print(f"zj = {zj}")  
            
            for i in range(len(zj)):
                # print(type(func[i]))
                if type(self.func[i])!=value1:
                    dj.append(M(self.func[i].get_const(),0)-zj[i])
                else:
                    dj.append(self.func[i].get_m()-zj[i])    
            # print(f"dj = {dj}")
            

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
                for i in range(len(self.usl)):
                    l=self.bi[i]/self.usl[i][r]
                    br1.append(l)
                # print(f"br1 = {br1}") 
                s=min(br1)
                br1.clear()
                print(f"s = {s+1}") 

            # Новые базисные перемнные
                for i in range(len(self.usl[s])): self.usl[s][i].baz=False
                self.usl[s][r].baz=True
                bp[s]=self.usl[s][r].get_per()
                # print(f"bp = {bp}")

            # Новые коефициенты базисных переменных    
                ci.clear()
                for i in bp:
                    for j in self.func:
                        if i==j.get_per():
                            if type(j)==value1:
                                ci.append(j.get_m()) 
                            else: ci.append(M(j.get_const(),0))
                # print(f"ci = {ci}")            

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
                        
                # print(f"func = {self.func}")               
                # print2(self.usl) 
                # print(f"bi = {self.bi}")

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

            print("=============================================================================")
            print("=============================================================================")
            # print("ОПТИМАЛЬНОЕ РЕШЕНИЕ:")
            result=dict(zip(bp,self.bi))
            mas.clear()
            self.result={}
            for i in range(self.n):
                p="X"+str(i+1)
                if p in result:
                    # print(f'{p}={result[p]}')
                    self.result[p]=result[p]
                else:
                    # print(f'{p}={0}')    
                    self.result[p]=0
    def get_result(self):
        result=[]
        keys=list(self.result.keys())    
        for i in keys:
            result.append(self.result[i])
        return result    


dimension=2
m=2
func=[1,-1]
usl=[
    [-1,2,'>=',4]
    ,[3,2,'<=',14]
]
sim=simplex(func,usl,dimension,m)
print(sim.result)
print(sim.get_result())