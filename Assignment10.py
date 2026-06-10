
li=[1,2,3,4,5]
sum=0
for i in li:
    sum=sum+i
print("sum of element",sum)


li=[60,20,30,40,50]
min=li[0]
max=li[0]
for i in li:
    if(i<=min):
        min=i
    elif(i>=max):
        max=i
print(max)
print(min)


li=[10,20,30,40,50]
max1=li[0]
second=0
for i in li:
    if(i>=max1):
        
        second=max1
        max1=i
        
    elif(i>second) and i!=max1:
        second=i


        # max2=max
print(second)
#print(max1)


li=[1,2,3,4,5,6]
res=li[::-1]
print(res)

li=[1,2,3,4,5,6]
n=int(input("enter a no:"))
count=0
for i in li:
    if(n==i):
        count=count+1
if count>0:
    print(f"no {n} is present ",count,"times")
else:
    print("not present in the list")

li=[1,2,3,4,4,2]
newli=[]
for i in li:
    if i not in newli:
        newli=newli+[i]
print(newli)

li=[1,2,3]
cube=[]
for i in li:
    cube=cube+[i*i*i]
print(cube)

li=[1,2,3,45,5,6]
even=[]
odd=[]
for i in li:
    if i%2==0:
        even=even+[i]
    else:
        odd=odd+[i]
print("even",even)
print("odd",odd)

li=[2,3,4,6,8]
m=int(input("enter a  m no:"))
n=int(input("enter a  n no:"))
for i in li:
    if(i%m==0 and i%n==0):
        print(i)

li=[1,2,3,4,5]
cube=[]
square=[]
for i in li:
    cube=cube+[i*i*i]
    square=square+[i*i]
print("square",square)
print("cube",cube)

li=[1,2,3,4,5,6]
odd=[]
for i in li:
    if(i%2!=0):
        odd=odd+[i]
print("odd",odd)