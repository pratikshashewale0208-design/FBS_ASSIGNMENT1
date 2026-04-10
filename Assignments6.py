for i in range(1,6):
    for j in range(1,6):
        if(j<=i):
            print(i,end=" ")
        else:
            print(" ",end=" ")
    print()
# Output
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
for i in range(1,6):
    for j in range(1,i+1):
        print(chr(64+j),end=" ")
        
    print()
# Output:
# A
# A B
# A B C
# A B C D
# A B C D E


for i in range(1,6):
    for j in range(1,6):
        if i==1 or i==5 or j==1 or j==5:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
# Output:
# * * * * *
# *       *
# *       *
# *       *
# * * * * *
n=1
for i in range(1,6):
    for j in range(1,6):
        if(j<=i):
            if(n<=10):
                print(n,end=" ")
                n=n+1
            else:
                print(" ",end=" ")
    print()

# Output:
# 1
# 2 3
# 4 5 6
# 7 8 9 10



for i in range(1,6):
    for j in range(1,10):
        if(j>=6-i and j<=4+i):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
# Output:
#         *
#        * *
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *

for i in range(1,6):
    for j in range(1,6):
        if j<=i:
            print(chr(64+j),end=" ")
        else:
            print(" ",end=" ")
    print()
# Output:
# A
# A B
# A B C
# A B C D
# A B C D E


for i in range(1,6):
    n=1
    for j in range(1,10):
        if(j>=6-i and j<=4+i):
            print(n,end=" ")
            n=n+1
        else:
            print(" ",end=" ")
    print()
# Output
#         1
#       1 2 3
#     1 2 3 4 5
#   1 2 3 4 5 6 7
# 1 2 3 4 5 6 7 8 9

for i in range(1,6):
    ch=65
    for j in range(1,10):
        if(j>=6-i and j<=4+i):
            print(chr(ch),end=" ")
            ch=ch+1
        else:
            print(" ",end=" ")
    print()
# Output:
#         A
#       A B C
#     A B C D E
#   A B C D E F G
# A B C D E F G H I