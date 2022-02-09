a,b,c = map(int,input().split())

def Calc(a,b):
    if b==1:
        return a%c
    temp =Calc(a,b//2)
    if b%2==0:
        return temp*temp%c
    else:
        return temp*temp*a%c
print(Calc(a,b))