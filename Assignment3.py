
#Assignment3
n=int(input("enter a no:"))
if(n>0):
    print("Positive")
else:
    print("Negative")
#     Output:
# enter a no:4
# Positive

c=input("Enter any alphabet:")
if c in("a,e,i,o,u"):
    print("its ovels")
else:
    print("its consonant:")



a = int(input("Enter 1st :"))
b = int(input("Enter 2nd: "))
c = int(input("Enter 3rd: "))

if a + b + c == 180:
    print("Valid Triangle")
else:
    print("Invalid Triangle")
# Output:
# Enter 1st :150
# Enter 2nd: 34
# Enter 3rd: 23
# Invalid Triangle


a = int(input("Enter side1: "))
b = int(input("Enter side2: "))
c = int(input("Enter side3: "))
if a + b > c and b + c > a and a + c > b:
    print("Valid Triangle")
else:
    print("Invalid Triangle")

a=int(input("Enter a 1st side:"))
b=int(input("Enter a 2nd side:"))
c=int(input("Enter a 3rd side:"))
if(a==b==c):
    print("its equilateral ")
elif a==b or b==c or a==c:
    print("its iscosceles")
else:
    print("its scalene")
# Output:
# Enter a 1st side:34
# Enter a 2nd side:33
# Enter a 3rd side:22
#  its scalene


u=input("enter username:")
p=input("enter password:")
if u=="pratiksha" and p=="1234":
    
    print("password and username is correct")
else:
    print("password and username is incorrect")
# Output:
# enter username:pratiksha
# enter password:1234
# password and username is correct

sub1=int(input("Enter 1st subject marks:"))
sub2=int(input("Enter 2nd subject marks:"))
sub3=int(input("Enter 3rd subject marks:"))
sub4=int(input("Enter 4th subject marks:"))
sub5=int(input("Enter 5th subject marks:"))
total=sub1+sub2+sub3+sub4+sub5
percentage=total/5
print("Percentage",percentage)
if percentage >=80:
    print("Grade A")
elif percentage >=65:
    print("Grade B")
elif percentage >=50:
    print("Grade c")
else:
    print("Failed")
# Output:
# Enter 1st subject marks:66
# Enter 2nd subject marks:76
# Enter 3rd subject marks:56
# Enter 4th subject marks:87
# Enter 5th subject marks:66
# Percentage 70.2
# Grade B

n=int(input("enter a three digit:"))
temp=n
d1=temp%10
temp=temp//10
d2=temp%10
temp=temp//10
d3=temp%10
rev=d1*100+d2*10+d3
if(rev==n):
    print("palindrome")
else:
    print("non palindrome")
# Output:
# enter a three digit:121
# palindrome

#

gender=input("Enter Gender:")
age=int(input("Enter a age:"))
if(gender=="famale" or age>=18) and (gender=="male" or age>=21):
    print("eligible for marriage")
else:
    print("wait for some time.....")
# Output:
# Enter Gender:male
# Enter a age:22
# eligible for Voting

sp=int(input("Enter a amount1:"))
cp=int(input("Enter a amount2:"))
if sp>cp:
    profit=sp-cp
    print("Profit is:",profit)
if cp>sp:
    loss=cp-sp
    print("loss is:",loss)

# Output:
# Enter a amount1:3000
# Enter a amount2:200
# Profit is: 2800

uc=int(input("Enter a unit charge:"))
bill=0
if uc<50:
    bill=uc*0.50
    elif uc<100:
        bill=uc*0.75
    elif uc<