#Test3
n=int(input("enter a no:"))
for i in range(2,n):
    if (n%i!=0):
        print("all prime no:",i)
# Output:
# enter a no:10
# all prime no: 3
# all prime no: 4
# all prime no: 6
# all prime no: 7
# all prime no: 8
# all prime no: 9

for i in range(1,7):
    for j in range(1,6):
        if (i+j)%2==0:
            print("1",end=" ")
        else:
            print("0",end=" ")

    print("")
# Output:
# 1 0 1 0 1
# 0 1 0 1 0
# 1 0 1 0 1
# 0 1 0 1 0
# 1 0 1 0 1
# 0 1 0 1 0

n=int(input("enter a no:"))
fact=1
sum=0
for i in range(1,n+1):
    fact=fact*i
    sum=sum+(i/fact)
print("sum=",sum)

n=int(input("Enter a no:"))
total=0
for i in range(1,n+1):
    n2=int(input("Enter basic salary"))
    if n2<2000:
        da=0.10*n2
        ta=0.12*n2
        hra=0.20*n2
    else:
        da=0.15*n2
        ta=0.18*n2
        hra=0.20*n2
    total=n2+da+ta+hra
    print("total salary:",total)
    t=total+1
print("total salary of employee:",t)

# Output:
# Enter a no:2
# Enter basic salary1000
# total salary: 1420.0
# Enter basic salary30000
# total salary: 45900.0
# total salary of employee: 45901.0