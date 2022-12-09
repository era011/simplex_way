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
    def set_const(self,c):
        self.c=c
    def __add__(self,other):
        return  value(self.c+other.c,self.get_index())  
    def __mul__ (self,other):
        return  value(self.c*other.c,self.get_index()) 
    def __truediv__(self,other):
        return value(self.c/other.c,self.get_index())
    def __sub__ (self,other):
        return  value(self.c-other.c,self.get_index())              

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
        return  M(other.c1+self.c1,other.b()+self.b())
    def __sub__(self,other):
        return  M(self.c1-other.c1,self.b()-other.b())    
    def __mul__ (self,other):
        s=self.c1*other.c1
        s1=self.b()*other.c1
        return  M(s,s1)
    def proverka(self)->int:
        return self.b()+self.c1

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
          