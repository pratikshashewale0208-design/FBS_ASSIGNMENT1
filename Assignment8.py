#Assignment 8
def area_rectangle(length,width):
    area=length*width
    return area
res=area_rectangle(5,3)
print("area of rectangle",res)


def area_circle(radius):
    area=3.14*radius*radius 
    return area
res=area_circle(4)
print("area circle",res)

def sos(n):
    total=0
    for i in range(1,n+1):
        total=total+i
    return total
res=sos(5)
print(res)

def prime(n):
    total = 0
    for i in range(2, n+1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            total += i
    return total
res=prime(10)
print(res)


def odd(n):
    total=0
    for i in range(1,n+1):
        if n%2!=0:
            total=total+i
    return total
res=odd(10)
print(res)

#fibbonacci
def fibbonacci(n):
    a=0
    b=1
    for i in range(n+1):
        print(a)
        a,b=b,a+b
        
print(fibbonacci(5))

def reverse(n):
    rev=0
    while n>0:
        digit=n%10
        rev=rev*10+digit
        n=n//10
    return rev
res=reverse(123)
print(res)


def leap(n):
    if (n%4==0 and n%100!=0) or (n%400==0):
        return "leap year"
    else:
        return "not leap year"
res=leap(2026)
print(res)

def armstrong(n):
    temp=n
    power=len(str(n))
    total=0
    while temp>0:
        digit=temp%10
        total +=digit**power
        temp//=10
    return total==n
print(armstrong(153))
