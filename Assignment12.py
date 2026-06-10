# ##########################Assignment12#############################
# str="pratiksha"
# print(str.replace("a","$"))
# 222222222222222222222222222222222222222222222222222222222222222222222222
# ind=int(input("Enter a index:"))
# str="python"
# new=str[:ind]+str[ind+1:]
# print(new)
# 33333333333333333333333333333333333333333333333333333333333333333333333
# str1="listen"
# str2="silent"
# if set(str1)==set(str2):
#     print("Anagrams")
# else:
#     print("non anagrams")
# 4444444444444444444444444444444444444444444444444444444444444444444444444
# str="silent"
# str1="listen"
# if(sorted(str)==sorted(str1)):
#     print("Anagrams")
# else:
#     print("Non Anagrams")
# 44444444444444444444444444444444444444444444444444444444444444444444444444
# str="pratiksha"
# if len(str)>1:
#     new=str[-1]+str[1:-1]+str[0]
    
# print(new)
# #    res=str[1],str[-1]=str[-1],str[1]
# # print(res)
# 5555555555555555555555555555555555555555555555555555555555555555555555555555
# str="praei"
# count=0
# for i in str:
#     if i in "aeiou":
#         count+=1
# print("Vowels count is",count)
#66666666666666666666666666666666666666666666666666666666666666666666666666666666
# str=input("enter a string:")
# res=str.replace(" ","_")
# print(res)
#77777777777777777777777777777777777777777777777777777777777777777777777777777777
# str="pratiksha"
# count=0
# for i in str:
#     if i in str:
#         count+=1
# print(count)
#88888888888888888888888888888888888888888888888888888888888888888888888888888888888
# str="pratiksha"
# res=""
# for i in range(len(str)):
#     if i%2==0:
#         res+=str[i]
# print(res)
#9999999999999999999999999999999999999999999999999999999999999999999999999999999999999
# str="pratiksha shewale"

# words=len(str.split())
# char=len(str)
# print(words)
# print(char)
# #101010101010101010101001010101010101010101010101010101010101011011010101010101010101010
# str1=input("enter first string:")
# str2=input("enter second string:")
# if(len(str1)>len(str2)):
#     print(str1)
# else:
#     print(str2)
##1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
str="pratiks a"
print(str.replace(" ","_"))
#12121211212121212121212121212121212121212212121212121212121212121212112121212121212121212
str="Pratiksha"
count=0
for i in str:
    if i.islower():
        count+=1
print(count)
#13131313131313113113131313131131311313113131311331311313131313113113131313131313131313131
str="prat2221"
alpa=0
digit=0
for i in str:
    if i.isalpha():
        alpa+=1
    elif i.isdigit():
        digit+=1
print("charactercount",alpa)
print("digit count",digit)
#1414141414141411414114141414111414444414444414141141141141414114141414141441414141414141
str="pratiksha pratiksha"
words=str.split()
for i in words:
    print(i,":",words.count(i))



