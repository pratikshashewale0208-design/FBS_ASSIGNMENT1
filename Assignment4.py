n = int(input("enter a no:"))
for i in range(1, n+1):
    if i % 2 != 0 and i % 3 != 0:
        print(i)


n = int(input("Enter a no: "))
d = int(input("Enter a no: "))

for i in range(1, n+1):
    if i % d == 0:
        print(i)

start=int(input("enter a start no:"))
end=int(input("enter ending no:"))
for i in range(start,end+1):
    if i%7==0 and i%5==0:
        print(i)