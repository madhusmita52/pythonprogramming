#write a program to demonstrate the diggerence between a global and local variable.
x="Alex"
def MyFunc():
    x="Sydney"
    print(x)

print(x)    
MyFunc()
#Create a function that modifies a global variable inside it.
counter = 0
def increment_counter():
    global counter 
    counter += 1  
    print("Counter inside function:", counter)

print("Counter before function call:", counter)
increment_counter()
print("Counter after function call:", counter)
#show how to use global keyword to access and change a global variable
x="Python"
def Character_change():
    global x
    x="Java"
print("before convertion:",x)
Character_change()
print("after convertion:",x)    
#Write a program where local variable copies global variable
num1=123
def Myprogram():
    num2=num1 
    print("value of num2:",num2)
print("Value of num1:",num1)     
Myprogram()
#Create two functions :one modifies a global variable and another reads it.
x=123
def func1():
    global x
    x+=123
def func2():
    global y
    y=x
func1()
print("Value of x is",x)
func2()
print("Value of Y is",y)
#Show what happens if you try to access a local variable outside of its scope.
x="James"
def func3():
    x="Tyron"
print(x)
#wite a function with the same variable name in both local and global scopes and print both.
x = 10
def demonstrate_scope():
    x =20
    print("Local x:", x)
    global_x = globals()['x']
    print("Global x:", global_x)
demonstrate_scope()
print("Global x outside function:", x)
#write a function to check whether a global variable exists inside it without using global keyword.
a="123"
def MyFunc():
    print(a)
    print(type(a))
MyFunc()  
#Create a function with a parameter that has same name as a global variable and print both.
def MyFunc(s):
    print("Inside function :"+s)
s=input("Enter your name:")
MyFunc(s) 
#Write a function that calculates factorial of a number using global variables for storing results.
factorial_result = 1
def calculate_factorial(n):
    global factorial_result 
    factorial_result = 1 
    if n < 0:
        print("Factorial is not defined for negative numbers.")
    for i in range(1, n + 1):
        factorial_result *= i

    print(factorial_result)
x=int(input("Enter a number"))
calculate_factorial(x)    
#write a list comprehension in python to generate squares of numbers from 1 to 10.
squares = [x**2 for x in range(1, 11)]
print(squares)
#Generate a list comprehension to filter even numbers from1 to 20.
even=[x%2==0 for x in range(1,21)]
print(even)
#Generate a list of cube of odd numbers using list comprehension fro 1 to 20.
cubes_of_odd_numbers = [x**3 for x in range(1, 21) if x % 2 != 0]
print("Cubes of odd numbers from 1 to 20:", cubes_of_odd_numbers)
#Create a list comprehension to generate prime numbers from 1–50.
prime_numbers = [n for n in range(2, 51) if all(n % i != 0 for i in range(2, int(n**0.5) + 1))]
print("Prime numbers from 1 to 50:", prime_numbers)
#Convert all strings in a list to uppercase using list comprehension.
strings_list = ["hello", "world", "python", "list", "comprehension"]
uppercase_list = [string.upper() for string in strings_list]
print("Original List:", strings_list)
print("Uppercase List:", uppercase_list)
#Extract first letters of each word in a list using list comprehension.
words = ["apple", "banana", "cherry", "date"]
first_letters = [word[0] for word in words if word]  
print("First letters:", first_letters)
#Write a list comprehension to reverse each word in a list.
words = ["hello", "world", "python", "rocks"]
reversed_words = [word[::-1] for word in words]
print(reversed_words)
#Generate a list of tuples (number, square) for numbers 1–10.
number_square_list = [(num, num ** 2) for num in range(1, 11)]
print("List of tuples (number, square):", number_square_list)
#Create a list comprehension to find common elements between two lists.
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common_elements = [element for element in list1 if element in list2]
print("Common elements:", common_elements)




