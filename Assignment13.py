# student={"id":10,"Name":"Pratiksha","Class":"10"}
# key=input("input a key:")
# value=input("Enter a Value:")
# res=update.student()
# print(student.items())
s=input("Enter a string:")
words=s.split()
d={}
for i in words:
    if i in d:
        d[i]+=1
    else:
        d[i]=1

print(d)

print("********************************************************************************")
Student={"name":"pratiksha","Roll_no":22}#\\
key=input("Enter a Key:")
Student.pop(key)
print(Student)
print("______________________________________________________________________________________")

d={'a':2,'b':3,'c':4}
mul=1
for i in d.values():
    mul=mul*i
print(mul)
print("________________________________________________________________________________________")

d={'a':2,'b':3,'c':5}
s=sum(d.values())
print(s)

print("_____________________________________________________________________________________________")
n=int(input("Enter N:"))
d={}
for i in range(1,n+1):
    d[i]=i*i
print(d)
print("________________________________________________________________________________________________")
d={'a':10,'b':20,'c':30}
key=input("enter key :")
if key in d:
    print("key exist")
else:
    print("Key doesnot exist")


print("________________________________________________________________________________")

d1={'a':10,'b':20,'c':40}
d2={'d':50,'e':80}
d1.update(d2)
print(d1)

print("____________________________________________________________________________________")


d={'a':10,'b':20}
key=input("enter a key")
value=int(input("enter a value"))
d[key]=value
print(d)