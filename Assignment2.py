
#Assignment 2
h=int(input("Enter a hours:"))
m=int(input("Enter a minutes:"))
s=int(input("Enter a second:"))
seconds=h*3600+m*60+s
print("Total Seconds",seconds)
# Output:
# Enter a hours:70
# Enter a minutes:267
# Enter a second:77
# Total Seconds 268097

# c=int(input("Enter a celcius:"))
# f=i
 
l=int(input("enter a length:"))
b=int(input("enter a breadth:"))
h=int(input("enter  height:"))
b=int(input("enter  base:"))

area_of_rectangle=l*b
area_of_triangle=0.5*b*h
print("Area of Rectangle:",area_of_rectangle)
print("Area of Rectangle:",area_of_triangle)
# Output:
# enter a length:4
# enter a breadth4
# enter  height:5
# enter  base:5
# Area of Rectangle: 20
# Area of Rectangle: 12.5

n=int(input("enter a three digit:"))
temp=n
d1=temp%10
temp=temp//10
d2=temp%10
temp=temp//10
d3=temp%10

sum=d1+d2+d3
print("sum of digit",sum)
# Output:
# enter a three digit:334
# sum of digit 10
#with third variable
n=int(input("enter a first no:"))
n1=int(input("enter a second no:"))
C=n
n=n1
n1=C
print("swapping two no:",n,n1)
# #Output:
# enter a first no:4
# enter a second no:6
# swapping two no: 6 4
#without variable
n=int(input("enter a first no:"))
n1=int(input("enter a second no:"))
n=n+n1
n1=n-n1
n=n-n1
print("swapping two no:",n,n1)
# Output:
# enter a first no:6
# enter a second no:7
# swapping two no: 7 6

n=int(input("enter a three digit:"))
temp=n
d1=temp%10
temp=temp//10
d2=temp%10
temp=temp//10
d3=temp%10
rev=d1*100+d2*10+d3

print("reversed no is:",rev)
# Output:
# enter a three digit:456
# reverser no is: 654

f=int(input("enter a f:"))
c/5=(f-32)/9
print("Temprature in celsius:",c)
# Output:
# enter a f:33
# Temprature in celsius: 0.5555555555555556

c=int(input("enter cost price:"))
d=int(input("enter a discount:"))
selling_price=c-d
print("selling Price is:",selling_price)
# Output:
# enter cost price:400
# enter a discount:50
# selling Price is: 350
b = float(input("Enter basic salary: "))

da = 0.10 * b
ta = 0.12 * b
hra = 0.15 * b

total_salary = b + da + ta + hra

print("DA =", da)
print("TA =", ta)
print("HRA =", hra)
print("Total Salary:", total_salary)

Output:
Enter basic salary: 2000
DA = 200.0
TA = 240.0
HRA = 300.0
Total Salary: 2740.0