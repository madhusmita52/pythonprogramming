#local variable example
def func():
    x=15
    print("Local x:",x)
func()
#global variable
x=25
def func():
    print("Global x:",x)
func()
#modify global variable
x=5
def func():
    global x
    x=x+10
func()
print("Modified global x:",x)
#local vs global with same name
x=100
def func():
    x=50
    print("Local:",x)
func()
print("Global:",x)
#using global inside fuction
y=40
def update():
    global y
    y=60
update()
print(y)  
#list comprehension
new_list=[i for i in range(20) if i%5==0]
print(new_list)
#odd
new_list=[i for i in range(20) if i%3==1]
print(new_list)
#dictionary comprehension
numbers=list(range(10))
new_dict_comp={n:n*3 for n in numbers if n%2==1}
print(new_dict_comp)
#
numbers=list(range(20))
new_dict_comp={n:n*4 for n in numbers if n%2==0}
print(new_dict_comp)
#zip and unzip
name=["Rishi","Laren","Liza","Roja"]
roll_no=[7,1,9,2]
marks=[90,80,60,70]
mapped=zip(name,roll_no,marks)
print(mapped)
mapped=set(mapped)
print(mapped)
namez,roll_noz,marksz=zip(*mapped)
print(namez)
print(roll_noz)
print(marksz)
#SORTING
fruits=['mango','sugarcane','corn','apple','strawberry']
sorted(fruits)
sorted(fruits,reverse=True)
sorted(fruits,key=len,reverse=True)
sorted(fruits,key=len)
sorted(fruits)
print(fruits)
fruits.sort()
#