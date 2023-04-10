from simplex import simplex

def ost(n):
    # print(type(n))
    return n-int(n)

def check_int(d):
    if type(d)!=str:
        keys=list(d.keys())
        for i in keys:
            # print(d[i])
            if ost(d[i])!=0:
                return i
        return -1    
    else: return  -1    

def f_val(func,res):
    if type(res)!=str:
        keys=list(res.keys())
        mas=[]
        result=0
        for i in keys:
            mas.append(res[i])
        for i in range(len(mas)):
            result+=mas[i]*func[i]
        return result           
    else:
        return 'нет решения'

def BandB(func,usl,otvety:list):
    zlp=simplex(func,usl1=usl)
    result=zlp.get_result()
    per=check_int(result)
    if per==-1:
        otvety.append([result,f_val(func,result)])

        print(f'ended-----------------------------------------------------------------------------------')
    else:
        per1=int(per[-1])-1
        new_bord=[]
        for i in range(len(usl[0])):
            new_bord.append(0)
        new_bord[per1]=1
        new_bord[-1]=int(result[per])
        new_bord[-2]='<='
        usl1=usl.copy()
        usl1.append(new_bord)
        index=len(usl)-1
        BandB(func,usl1,otvety)
        # usl1.clear()
        # usl1=usl.copy()
        usl1.pop()
        new_bord.clear()
        for i in range(len(usl[0])):
            new_bord.append(0)
        new_bord[per1]=1    
        new_bord[-1]=int(result[per])+1
        new_bord[-2]='>='
        usl1.append(new_bord)
        # for i in range(len(usl)-index):
        #     usl.pop()
        BandB(func,usl1,otvety)
        usl1.pop()

    # keys=list(result.keys())
    # for i in keys:
        # if ost(result[i])!=0:


# func=[1,-1]
# usl=[
#     [-1,2,'>=',4]
#     ,[3,2,'<=',14]
# ]
# (2,3)  -1

# func=[2,-8]
# usl=[
#     [1,2,'<=',16]
#     ,[6,2,'<=',40]
# ]
# (6,0) 12


# func=[-1,-1]
# usl=[
#     [1,-2,'<=',0]
#     ,[1,-1,'>=',-1]
#     ,[1,0,'>=',0.75]
# ]

# func=[2,-1]
# usl=[
#     [1,-2,'<=',0]
#     ,[1,-1,'>=',-1]
#     ,[1,1,'<=',3.2]
# ]

# func=[10,1]
# usl=[
#     [-1,0.5,'>=',1]
#     ,[2,1,'<=',6]
# ]
# (1,4)  14

# func=[2,4]
# usl=[
#     [2,1,'<=',19/3]
#     ,[1,3,'<=',10]
# ]
# (1,3)   14

# func=[1,1]
# usl=[
#     [-1,1/2,'<=',1/2]
#     ,[2,1,'<=',6]
# ]
# (1,3)  4
# (2,2)  4

func=[1,-1]
usl=[
    [-1,2,'<=',4]
    ,[3,2,'<=',14]
]
# (4,0)  4


otvety=[]
BandB(func,usl,otvety)
for i in otvety:
    print(i)