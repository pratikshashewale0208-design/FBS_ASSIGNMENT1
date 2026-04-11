for i in range(1,6):
    for j in range(1,6):
        if(j<=i):
            if i==1 or i==5 or j==1 or j==i:
                 print("*",end=" ")
            else:
                 print(" ",end=" ")
    print()
# Output:
# *
# * *
# *   *
# *     *
# * * * * *

for i in range(1,6):
    n=i
    for j in range(1,10):
        
        if(j>=6-i and j<=4+i):
            
            print(n,end=" ")
            if j<5:
                n=n+1
            else:
                n=n-1
        else:
            print(" ",end=" ")
    print()
# Output:
#         1
#       2 3 2
#     3 4 5 4 3
#   4 5 6 7 6 5 4
# 5 6 7 8 9 8 7 6 5

for i in range(1,6):
    for j in range(1,6):
        if i==1:
            print(j,end=" ")
        elif j==1:
            print(i,end=" ")
        elif j==6-i:
            print(5,end=" ")
                
        else:
            print(" ",end=" ")
    print()
# Output:
# 1 2 3 4 5
# 2     5
# 3   5
# 4 5
# 5

for i in range(1,6):
    n=1
    for j in range(1,10):
        if(j>=6-i and j<=4+i):
            print(n,end=" ")
            if j<5:
                n=n+1
            else:
                n=n-1
        else:
            print(" ",end=" ")
    print()
#     Output:
#        1
#       1 2 1
#     1 2 3 2 1
#   1 2 3 4 3 2 1
# 1 2 3 4 5 4 3 2 1


for i in range(1,6):
    for j in range(1,6):
        if(j<=i):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
for i in range(1,5):
    for j in range(1,5):
        if(j<=5-i):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
# Output:
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *




n = 5

for i in range(1, n + 1):
    
    for s in range(n - i):
        print(" ", end="")

    
    for j in range(1, i + 1):
        if j == 1 or j == i or i == n:
            print(j, end=" ")
        else:
            print(" ", end=" ")

    print()
# Output:
#     1
#    1 2
#   1   3
#  1     4
# 1 2 3 4 5