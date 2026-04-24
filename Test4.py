def factor(n):
    for i in range(1,n):
        if(n%i==0):
            print(i)
n=10
res=factor(n)
print(n)

#factorial
def factorial(n):
    if(n==0):
        return 0
    else:
        return n*factorial(n-1)
n=10
res=factorial(n)
print(res)


for i in range(1,20):
    for j in range(1,20):
        if(i==1 or i==20-1 or i+j==20-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

   
