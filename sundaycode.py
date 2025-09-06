#Print nos 1 to 11
i=1
for i in range(1,11):
    print(i)
#Print even nos 1 to 20
for i in range(1,21):
    if i%2==0:
        print(i)
#Print odd nos 1 to 20
for i in range(1,21):
    if i%2!=0:
        print(i)
#Print first 10 squares
for i in range(1,11):
    print(i**2)
#Print first 10 cubes
for i in range(1,11):
    print(i**3)
#Print multiplication table of 5
for i in range(1,11):
    print(i*5)
#Print sum of first 10 nos
sum=0
for i in range(1,11):
    sum+=i
print(sum)
#Print factorial of n
fact=1
n=int(input("Enter a number:"))
for i in range(1,n+1):
    fact*=i
print(fact)
#Print reverse counting 10 to 1
for i in range(10,1,-1):
    print(i)
#Print first 10 fibonacci nos
num1=0
num2=1
print(num1)
print(num2)
for i in range(3,11):
    num3=num1+num2
    num1=num2
    num2=num3
    print(num3)
#Print star in line
for i in range(5):
    print("*")
#Print squares pattern
for i in range(1,6):
    for j in range(1,6):
        print("*",end=" ")
    print()
#Print abc
for i in range(1,5):
    print("abc "*5)
#Print right triangle
for i in range(6):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
#Print inverted triangle
for i in range(5,0,-1):
    print("* "*i)
#Print no triangle
for i in range(6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
#Print reverse no triangle
for j in range(5,0,-1):
    for i in range(1,j+1):
        print(i,end=" ")
    print()
#Count vowels in a string
vowels="aeiouAEIOU"
count=0
s=input("Enter your name:")
for ch in s:
    if ch in vowels:
        count+=1
print(count)
#Reverse a string
rev=""
s=input("Enter your name:")
for ch in s:
    rev=ch+rev
print(rev)
#Count lowercase letters
count=0
s=input("Enter you name:")
for ch in s:
    if ch.islower():
        count+=1
print(count)
#Count uppercase letters
count=0
s=input("Enter your name:")
for ch in s:
    if ch.isupper():
        count+=1
print(count)
#Print multiplication tables from 1 to 10
for i in range(1,11):
    for j in range(1,11):
        print(i*j,end=" ")
    print()
#Print checkerboard pattern
for i in range(5):
    for j in range(5):
        if(i+j)%2==0:
            print("X",end=" ")
        else:
            print("O",end=" ")
    print()
#Print each character of a string

s=input("Enter your name:")
for ch in s:
    print(ch)
#   