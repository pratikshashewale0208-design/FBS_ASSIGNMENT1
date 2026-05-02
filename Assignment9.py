#Assignment 9
#sum of series 
def sos(n):
    if n==0:
        return 0
    else:
        return n+sos(n-1)
n=5
res=sos(n)
print(res)

# Prime no
def prime(n,i=2):
    if n<=1:
        return "not prime"
    if i==n:
        return "Prime"
    if n%i==0:
        return "Not prime"

    return prime(n,i+1)
n=5
res=prime(n)
print(res)    


#reverse
def reverse(n):
    if n==0:
        return 0
    
    return n%10 +reverse(n//10)
n=1234
res=reverse(n)
print(res)

def reverse(n):
    if n==0:
        return
    print(n%10,end="")
    reverse(n//10)   
n=1234
res=reverse(n)
print(res)

#armstrong number
def armstrong(n,power):
    if(n==0):
        return 0
    digit=n%10
    return (digit** power)+armstrong(n//10,power)
num=(153)
power=len(str(num))
res=armstrong(num,power)
if res==num:
    print("armstrong")
else:
    print("non armstrong")


n=int(input("enter a no:"))
sum=0
temp=n
while(n>0):
    r=n%10
    sum=sum+(r*r*r)
    n=n//10
if (temp==sum):
    print("armstrong no:")
else:
    print("non armstrong")

def sumofdigit(n):
    sum=0
    if n==0:
        return 0

    return (n%10)+sumofdigit(n//10)
n=123
res=sumofdigit(n)

print(res)
#factorial
def factorial(n):
    if(n==0):
        return 1
    return n*factorial(n-1)
n=5
res=factorial(5)
print(res)

#fibbonacci
def fibbonacci(n):
    if(n==0):
        return 0
    return n+fibbonacci(n-1)
n=5
res=fibbonacci(5)
print(res)

def power(m,n):
    if(n==0):
        return 1
    return m*power(m,n-1)
m=5
n=3
res=power(m,n)
print(res)