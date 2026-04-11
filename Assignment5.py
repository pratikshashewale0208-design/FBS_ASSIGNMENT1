#Assignment5
user="Pratiksha"
password="1234"
for i in range(3):
    u=input("Enter username:")
    p=input("Enter password:")
    if u==user and p==password:
        print("Login Succefully:")
        break
    else:
        print("Wrong passwords:")
else:
    print("terminated")

n=int(input("Enter 1st subject marks:"))
total=0
for i in range(1,n+1):
    print(i)
    total=0
    for j in range(1,6):
        marks=float(input(f"Enter marks {j}:"))
        total +=marks
    percent=total/5
    print("percentage=",percent)
    total +=percent
avg=total/n
print("average percentage:",avg)


for i in range(2,101):
    count=0
    for j in range(1,i+1):
        if num%i==0
        count +=1
    if count==2:
        print(n)


n=int(input("enter a no:"))
fact=1
sum=0
for i in range(1,n+1):
    fact=fact*i
    sum=sum+(i/fact)
print("sum=",sum)


#armstrong
start = int(input("Enter start: "))
end = int(input("Enter end: "))

for num in range(start, end+1):
    temp = num
    s = 0
    
    while temp > 0:
        d = temp % 10
        s += d**3
        temp //= 10
    
    if s == num:
        print(num)