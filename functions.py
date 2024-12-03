#function in python
# a=9
# b=8
# gmin1 = (a*b)/(a+b)
# print(gmin1)
# if(a>b):
#     print("first is greater")
# else:
#     print("second is greater")    

# c=10
# d=15
# gmin2 = (c*d)/(c+d)
# print(gmin2)

def calculategmin(a,b):
    mean = (a*b)/(a+b)
    print(mean)
def greater(a,b):
    if(a>b):
        print("first is greater")
    else:
        print("second is greater")    
def lesser(a,b):
    pass

a=20
b=30
calculategmin(a,b)
greater(a,b)

c=60
d=40
calculategmin(c,d)
greater(c,d)

##function arguments in python