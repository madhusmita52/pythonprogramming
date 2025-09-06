#create an from a list
my_list=[1,2,3]
it=iter(my_list)
print(next(it))
print(next(it))
print(next(it))
#ITERATOR WITH TUPLE
my_tuple=(10,20,30)
for val in iter(my_tuple):
    print(val)
#STRING ITERATOR
s="Python"
it=iter(s)
print(next(it))
print(next(it))
#USING WHILE WITH ITERATOR
nums=[1,2,3,4]
it=iter(nums)
while True:
    try:
        print(next(it))
    except StopIteration:
        break
#ITERATOR WITH RANGE
for x in iter(range(5)):
    print(x)
#ITERATOR OVER DICTIONARY KEYS
d={"a":1,"b":2}
for i in iter(d):
    print(i)
#ITERATOR OVER DICTIONARY ITEMS
for item in iter(d.items()):
    print(item)
#ITERATOR WITH SET
for s in set([1,2,2,3]):
    print(s)
#ITERATOR WITH SORTED
for x in sorted([5,1,4]):
    print(x)
#SIMPLE GENERATOR
def gen():
    yield 1
    yield 2
    yield 3
for x in gen():
    print(x)
#GENERATOR WITH RANGE
def my_range(n):
    for i in range(n):
        yield i
print(list(my_range(5)))
#GENERATOR EXPRESSION
gen=(x*x for x in range(5))
print(list(gen))
#EVEN NUMBERS
def even(n):
    for i in range(2,n+1,2):
        yield i
print(list(even(10)))
#ODD NUMBERS
def odd(n):
    for i in range(1,n+1,2):
        yield i
print(list(odd(10)))
#CHARACTERS OF STRING
def char_gen(s):
    for ch in s:
        yield ch
print(list(char_gen("Hello")))
#COUNTDOWN
def countdown(n):
    while n>0:
        yield n
        n-=1
print(list(countdown(5)))
#WRITE TO FILE
f=open("madhuliza.txt",'w')
f.write("hello madhu")
#READ FROM FILE
f=open("madhuliza.txt",'r')
print(f.read())
#APPEND TO FILE
f=open("madhusmita.txt",'a')
f.write("\nNew Line")
#CHECK IF FILE EXIST
import os
print(os.path.exists("madhuliza.txt"))
#FILE SIZE
print(os.path.getsize("madhuliza.txt"))
#READ FIRST FIVE CHARS
f=open("madhuliza.txt",'r')
print(f.read(5))
#SIMPLE TRY-EXCEPT 
try:
    x=10/0
except ZeroDivisionError:
    print("Cannot divide by zero")
#TRY-EXCEPT-FINALLY
try:
    print(1/1)
finall:
    print("Always runs")
#CATCHING ALL EXCEPTIONS
try:
    print(10/0)
except Exception as e:
    print("Error:",e)
#TYPE ERROR
try:
    print("2"+2)
except TypeError:
    print("Type mismatch")
#VALUE ERROR
try:
    num=int("xyz")
except ValueError:
    print("Not a number")
    