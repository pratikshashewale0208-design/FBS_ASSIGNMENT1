#Assignment1
s1=int(input("Enter a marks 1st sub:"))
s2=int(input("Enter a marks 2nd sub:"))
s3=int(input("Enter a marks 3rd sub:"))
s4=int(input("Enter a marks 4th sub:"))
s5=int(input("Enter a marks 5th sub:"))
total=s1+s2+s3+s4+s5
percentage=total/5
print("percentage of 5 sub",percentage)

# output:
# Enter a marks 1st sub:40
# Enter a marks 2nd sub:45
# Enter a marks 3rd sub:65
# Enter a marks 4th sub:87
# Enter a marks 5th sub:67
# percentage of 5 sub 60.8

length=int(input("Enter a length:"))
breadth=int(input("enter a breadth:"))
area_of_rectangle=length*breadth
print(f"Area of reactangle (length:{length} breadth:{breadth}):",area_of_rectangle)
# Output:
# Area of reactangle (length:6 breadth:4): 24

n=int(input("Enter a number:"))
m=int(input("Enter a number:"))
remainder=n%m
queotient=n//m
print("Remainder is:",remainder)
print("Queotient is:",queotient)
# Output:
# Remainder is: 0
# Queotient is: 10

P=int(input("Enter a Principal:"))
T=int(input("Enter a Time:"))
R=int(input("Enter a Rate:"))
Simple_Interest=(P*R*T)/100
print("Simple Interest:",Simple_Interest)
# Output:
# Enter a Principal:100
# Enter a Time:50
# Enter a Rate:2
# Simple Interest: 100.0

P=int(input("Enter a Principal:"))
T=int(input("Enter a Time:"))
R=int(input("Enter a Rate:"))
Amount=P*(1+R/100)**T
Compound_Interest=Amount-P
print("Compound Interest:",Compound_Interest)
# Output:
# Enter a Principal:1000
# Enter a Time:2
# Enter a Rate:5
# Compound Interest: 102.5

a=int(input("Enter a 1st Angle:"))
b=int(input("Enter a 2nd Angle:"))
c=180-(a+b)
print("Third Angle:",c)
# Output:
# Enter a 1st Angle:60
# Enter a 2nd Angle:60
# Third Angle: 60

d=int(input("Enter a Days:"))
year=d//360
week=(d//365)//7
day=(d%365)%7
print("Year:",year)
print("Week:",week)
print("day:",day)
# Output:
# Enter a Days:767
# Year: 2
# Week: 0
# day: 2

h=float(input("Enter a Height:"))
b=float(input("Enter a Base:"))
area_of_triangle=0.5*h*b
print("area of triangle:",area_of_triangle)
# Output:
# Enter a Height:10
# Enter a Base:5
# area of triangle: 25.0


h=float(input("Enter a Height:"))
b=float(input("Enter a Base:"))
area_of_triangle=0.5*h*b
print("area of triangle:",area_of_triangle)

r=float(int(input("Enter radius:")))
pi=3.14
volume=(4/3) *pi * r**3
print("volume of sphere:",volume)
# Output:
# Enter radius:3
# volume of sphere: 113.03999999999999


a=float(input("Enter side:"))
area = (1.732 / 4) * a * a
print("Area_of_Equilateral:",area)
# Output:
# Enter side:4
# Area_of_Equilateral: 6.928

r=int(input("Enter a radius:"))
c=2*3.14*r
print("circumference_of_circle",c)
# Output:
# Enter a radius:4
# circumference_of_circle 25.12