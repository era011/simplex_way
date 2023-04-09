from functions import*

class value:
    baz=False
    def __init__(self,c,i):
        self.per="X"+str(i+1)
        self.c=c
    def __repr__(self):
        if self.per[len(self.get_per())-1:]!="0":
            if self.baz:
                return "("+str(self.c)+"*"+self.per+")"
            else:
                return str(self.c)+"*"+self.per
        else: return str(self.c)     
    def get_per(self):
        return self.per 
    def get_index(self):
        return int(self.get_per()[1:])-1    
    def get_const(self):
        return self.c 
    def get_m(self):
        return self.c             
    def set_const(self,c):
        self.c=c
    def __add__(self,other):
        return  value(round(self.c+other.c,2),self.get_index())  
    def __mul__ (self,other):
        return  value(round(self.c*other.c,2),self.get_index()) 
    def __truediv__(self,other):
        return value(round(self.c/other.c,2),self.get_index())
        # if other.c!=0:
        #     return value(self.c/other.c,self.get_index())
        # else:
        #     return value(float('inf'),self.get_index())
    def __sub__ (self,other):
        return  value(round(self.c-other.c,2),self.get_index())              

class M:
    def __init__(self, c1,bm):
        self.c1=c1
        self.bm=str(bm)+'M'
    def __repr__(self):
        if not proverka_na_int(self.bm):
            return str(self.c1)
        elif (self.c1==0) and proverka_na_int(self.bm):
            return self.bm
        elif (self.bm[:1]!="-"):
            return str(self.c1)+"+"+self.bm
        else:
            return str(self.c1)+self.bm    
    def b(self):
        return float(self.bm[:-1])
    def get_const(self):
        return self.c1
    def __add__(self,other):
        if type(other)==M:
            return  M(round(other.c1+self.c1,2),round(other.b()+self.b(),2))
        else:
            return  M(round(other+self.c1,2),round(self.b(),2))
    def __sub__(self,other):
        return  M(round(self.c1-other.c1,2),round(self.b()-other.b(),2))    
    def __mul__ (self,other):
        if isinstance(other,M):
            # print('ki')
            s=self.c1*other.c1
            s1=self.b()*other.c1
        else:
            # print('ki')
            s=self.c1*other
            s1=self.b()*other    
        return  M(round(s,2),round(s1,2))
    def proverka(self)->int:
        # return self.b()+self.c1
        if self.b()!=0:
            return self.b()
        else:
            return self.c1

class value1:
    def __init__(self,c1,bm,i):
        self.m=M(c1,bm)
        self.per="X"+str(i)
    def __repr__(self):
        return str(self.m)+self.per
    def get_m(self):
        return self.m 
    def get_per(self):
        return self.per     
          