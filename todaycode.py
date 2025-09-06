my_list=[1,1,2,3,4,4,5,5,6,7]
my_set=set(my_list)
print(my_set)
set1={1,2,3}
set2={1,9,0}
intersection_set=set1.intersection(set2)
print(intersection_set)
#print the data type of an integer,float,string,boolean
a=5
b=6.7
c="madhu"
d=True
print(type(a))
print(type(b))
print(type(c))
print(type(d))
#Take user input and print its type
a=input("Enter your name:")
print(a)
print(type(a))
#Convert a float to int
b=6.5
print(b)
print(int(b))
#Convert an int to float
c=67
print(c)
print(float(c))
#Convert an int to string
a=34
print(a)
var1=str(a)
print(var1)
print(type(var1)) 
#Convert a string to int
a="33"
print(a)
var1=int(a)
print(var1)
print(type(var1))
#Add two integers
a=5
b=6
c=a+b
print(c)
#Add an integer and a float
a=22
b=45.4
c=a+b
print(c)
#Multiply two integer
a=33
b=23
c=a*b
print(c)
#Divide two integers and display flot result
a=22
b=11
c=a/b
print(float(c))
#Find mudules of two nos
a=22
b=11
c=a%b
print(c)
#Find power of a no using **
a=12
b=a**2
print(b)
#Calculate square root of a no
a=144
b=144**0.5
print(b)
#Take radius and calculate area of a circle
r=2
area=3.141*r**2
print(area)
#Swap two nos (with third variable)
a=12
b=22
c=a
a=b
b=c
print(a)
print(b)
#Swap two nos (without third variable)
a=33
b=45
a,b=b,a
print(a)
print(b)
#Find simple interest
p=int(input("Enter principal:"))
t=int(input("Enter time:"))
r=float(input("Enter rate of interest:"))
i=p*t*r/100
print(i)
#Find compound interest
 p=int(input("Enter principal:"))
 r=float(input("Enter rate :"))
 t=int(input("Enter time:"))
 a=(p*(1+r/100)**t)-p
 print(a)
 #Convert celcius to fahrenheit
 c=int(input("Enter Celcius what you want:"))
 f=(9/5*c)+32
 print(f"{c} degree celcius {f} degree farenhite")
 #Convert fahrenheit to celcius
 f=int(input("Enter Fahrenheit what you want:"))
 c=(f-32)*5/9
 print(c)
 #Print length of a string
 Name="MADHUSMITA"
 len(Name)
 #Concatenate two string
 var1="Hello World"
 var1
 var1+"Python"
 print("updated string:-",var1+"Python")
 #Repeat a string five times
for i in range(1,6):
     print("Madhu")
#Find first character of a string
Name="Madhu"
print(Name[0])
#Find last character of a string
Name="Madhu"
print(Name[4])
#Slice first 5 characters of a string
Name="MADHUSMITA"
print(Name[0:5])
#Reverse a string using slicing
a="Madhu"
b=a[-1:-6:-1]
print(b)
#Convert string to uppercase
Name="madhusmita"
print(Name.upper())
#Convert string to lowercase
Name="MADHUSMITA"
print(Name.lower())
#Capitalize the first letter of a string
Name="madhusmita"
print(Name.capitalize())
#Count occurrences of a character
string="Madhu is a student"
substring="a"
count=string.count(substring)
print("The count is :",count)
#Replace substring in a string
string="Madhu"
print(string.replace("M","G",1))
#Check if substring exists in a string 
string="Madhu is a innocent girl"
substring="is"
count=string.count(substring)
print("The count is :",count)
#Create a list of 5 nos
a=[1,2,3,4,5]
print(a)
#Print length of a list
a=[1,2,3,4,5]
#Append an element to a list
a=['123','abc','tommy']
a[2]=30
#Split a string into words

split1="Liza is a smart girl"
print(split1.split())
print("Updated a:",a)
a.append(20)
print("After append :",a)
print(len(a))
#Insert element at position in list
a=['123','tommy','abc']
a.insert(3,2008)
print("After inset:",a)
#Remove element from list
a=['abc','123','xyz']
print("popped element at Index 2:",a.pop())
print("list after pop:",a)
#sort a list
a=[12,66,87,33,23]
a.sort()
print(a)
#Join  list of words into a string
a=['he','is','a']
b=['student']
c=a+b
print(c)
#Reverse a list
a=['tommy','123','abc']
a.reverse()
print(a)
#Convert list to tuple
list1=[123,'xyz']
tup1=(tuple(list1))
print(tup1)
#Find maximum element in list
a=[123,34,56]
print(max(a))
#Find minimum element in list
a=[123,34,78,90]
print(min(a))
#Check if a string is numeric
str='madhu'
if string.isalpha():
    print("True")
else:
    print("False")
#Check if string contains only alphabet
str="madhu"
if str.isalpha():
    print("True")
else:
    print("False")


#Remove spaces from a string
a="Liza is working"
print(a.replace(" ",""))


#Remove vowels from a string
str="madhu"
print(str.replace("a","u"))


#check if no is zero or not
a=45
if a==0:
    print("Zero")
else:
    print(a)
#check if no is zero positive or negative
a=33
if a>0:
    print("positive")
elif a<0:
    print("negative")
else:
    print("zero")
#check if no is even odd
a=12
if (a/2==0):
    print("even")
else:
    print("odd")
#find largest of two nos
a=23
b=12
if a>b:
    print(a)
else:
    print(b)
#find smallest of two nos
a=23
b=44
if a<b:
    print(a)
else:
    print(b)
#find largest of 3 nos
a=45
b=34
c=67
if a>b&a>c:
    print(a)
elif b>a&b>c:
    print(b)
else:
    print(c)
#smallest in 3 nos
a=22
b=90
c=56
if a<b&a<c:
    print(a)
elif b<a&b<c:
    print(b)
else:
    print(c)
#check a no is divisible by 5
a=25
if (a%5==0):
    print("divisible")
#check if a no is divisible by 7
a=48
if (a%7==0):
    print("divisible")
else:
    print("not divisible")
#check if a no is divisible by both 3 and 5
a=15
if (a%3==0&a%5==0):
    print("divisible")
else:
    print("not")
#check if person is eligible to vote(age>=18)
ram=23
if ram>=18:
    print("eligible for vote")
else:
    print("not eligible")
#check if a no is a multiple of 10
a=100
if (a%10==0):
    print("yes")
else:
    print("no")
#check if a year is leap year or no
a=int(input("Enter year:"))
if (a%4==0):
    print("leap year")
else:
    print("not")
#check if character is vowel or constant
a='e'
if a in 'aeiou':
    print('Vowel')
else:
    print('not Vowel')

#check if entered character is uppercase
a="MADHU"
if a.isupper():
    print("True")
else:
    print("False")
#check if entered character is lowercase
a="madhu"
if a.islower():
    print("True")
else:
    print("False")
#check if character is alphabet or digit
#check if character is special character
var1=input("Enter a character:")
if not var1.isspace():
    print("is special character")
else:
    print("not")
#check if no is a two digit no
num=22
if (num>=10) and (num<=99):
    print("True")
else:
    print("False")
#check if no is three digit
num=333
if (num>=100) and (num<=999):
    print("True")
else:
    print("False")
#check if no is palindrome



#check pass/fail(marks>=40pass)
math=45
if (math>=40):
    print("Pass")
else:
    print("Fail")
#check if no is positive ,negative or zero
num=7
if (num>0):
    print("positive")
elif(num<0):
    print("negative")
else:
    print("zero")
#print biggest among four nos

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
num4 = int(input("Enter fourth number: "))

if num1 >= num2 and num1 >= num3 and num1 >= num4:
    print("Biggest number is:", num1)
elif num2 >= num1 and num2 >= num3 and num2 >= num4:
    print("Biggest number is:", num2)
elif num3 >= num1 and num3 >= num2 and num3 >= num4:
    print("Biggest number is:", num3)
else:
    print("Biggest number is:", num4)

# 71. Print grade based on marks.
marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
elif marks >= 60:
    print("Grade: D")
else:
    print("Grade: F")
#Find profit or loss (based on cost & selling price).
cost_price = float(input("Enter cost price: "))
selling_price = float(input("Enter selling price: "))
if selling_price > cost_price:
    profit = selling_price - cost_price
    print("Profit:", profit)
elif selling_price < cost_price:
    loss = cost_price - selling_price
    print("Loss:", loss)
else:
    print("No profit, no loss.")
#Print electricity bill (with slabs).
units = float(input("Enter units consumed: "))
if units <= 100:
    bill = units * 1.5
elif units <= 300:
    bill = 100 * 1.5 + (units - 100) * 2.5
else:
    bill = 100 * 1.5 + 200 * 2.5 + (units - 300) * 3.5
print("Electricity Bill:", bill)
#Print bonus if salary > 50000.
salary = int(input("Enter your salary: "))
if salary > 50000:
    print("Bonus")
else: 
    print("No Bonus")
#Check if triangle is equilateral, isosceles, or scalene.
side1 = float(input("Enter first side: "))
side2 = float(input("Enter second side: "))
side3 = float(input("Enter third side: "))

if side1 == side2 == side3:
    print("Triangle is equilateral.")
elif side1 == side2 or side2 == side3 or side1 == side3:
    print("Triangle is isosceles.")
else:
    print("Triangle is scalene.")
#Check if triangle is valid (sum of angles = 180).
angle1 = int(input("Enter first angle: "))
angle2 = int(input("Enter second angle: "))
angle3 = int(input("Enter third angle: "))

if angle1 + angle2 + angle3 == 180:
    print("Valid triangle.")
else:
    print("Invalid triangle.")

#Check if number is palindrome.
num = int(input("Enter a number: "))
temp = num
rev = 0
while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp //= 10
if num == rev:
    print("Number is palindrome.")
else:
    print("Number is not palindrome.")
#Check if number is between 1 and 100.
num = int(input("Enter a number: "))
if num > 1 and num < 100:
    print(f"{num} is between 1 and 100")
else:
    print(f"{num} is not between 1 and 100")
#Check if number is not divisible by 2 and 3.
num = int(input("Enter a number: "))
if num % 2 != 0 and num % 3 != 0:
    print(f"{num} is not divisible by 2 and 3")
else:
    print(f"{num} is divisible by 2 or 3")
#Check if string length is between 5 and 10.
string = input("Enter a string: ")
if len(string) >= 5 and len(string) <= 10:
    print("String length is between 5 and 10")
else:
    print("String length is not between 5 and 10")
#Check if a character is vowel and lowercase.
char = input("Enter a character: ")
if char in "aeiouAEIOU" and char.islower():
    print(f"{char} is a lowercase vowel.")
else:
    print(f"{char} is not a lowercase vowel.")
#Check if a year is century leap year.
year = int(input("Enter a year: "))
if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
#ATM withdrawal allowed only if balance > withdrawal amount.
balance = int(input("Enter your balance:"))
withdrawal_amount = int(input("Enter withdrawal amount:"))
if balance > withdrawal_amount:
    print("Withdrawal allowed.")
else :
    print("Withdrawal not allowed.")
#Check discount eligibility (bill > 1000).
bill = float(input("Enter total bill amount: "))
if bill > 1000:
    print("Eligible for discount.")
else:
    print("Not eligible for discount.")
#Check if entered password is correct.
actual_password = "Abcd@123"
password = input("Enter password: ")
if password == actual_password:
    print("Password is correct.")
else:
    print("Password is incorrect.")
#Print greeting based on time of day (morning, afternoon, evening).
time = int(input("Enter time (0-23): "))
if time < 12:
    print("Good morning!")
elif time < 18:
    print("Good afternoon!")
else:
    print("Good evening!")
#Calculate BMI and print category.
weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in meters: "))
bmi = weight / (height ** 2)
print("BMI:", bmi)
if bmi < 18.5:
    print("Category: Underweight")
elif bmi < 24.9:
    print("Category: Normal weight")
elif bmi < 29.9:
    print("Category: Overweight")
else:
    print("Category: Obesity")
#Check if person is teenager (13–19).
age = int(input("Enter your age: "))
if 13 <= age <= 19:
    print("You are a teenager.")
else:
    print("You are not a teenager.")
#Print day of week (1=Monday … 7=Sunday).
day = int(input("Enter day number (1-7): "))
if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")
else:
    print("Invalid day number.")
#Print month name for given number.
month = int(input("Enter month number (1-12): "))
if month == 1:
    print("January")
elif month == 2:
    print("February")
elif month == 3:
    print("March")
elif month == 4:
    print("April")
elif month == 5:
    print("May")
elif month == 6:
    print("June")
elif month == 7:
    print("July")
elif month == 8:
    print("August")
elif month == 9:
    print("September")
elif month == 10:
    print("October")
elif month == 11:
    print("November")
elif month == 12:
    print("December")
else:
    print("Invalid month number.")
#Check if given character is in your name.
char = input("Enter a character: ").lower()

name = "Madhusmita Malik"
if char in name.lower():
    print(f"{char} is in your name.")
else:
    print(f"{char} is not in your name.")
#Check if string is palindrome.
string = input("Enter a string: ").lower()
if string == string[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
#Check if entered string is "python".
string = input("Enter a string: ").lower()
if string == "python":
    print("The string is python.")
else:
    print("The string is not python.")
#Check if number is Armstrong number.
num = int(input("Enter a number: "))
sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10
if num == sum:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
#Check if number is Prime or not.
num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, num): 
        if num % i == 0:
            print(f"{num} is not a prime number.")
            break
    else:
        print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
    
#Check if number is Perfect number.
num = int(input("Enter a number: "))
sum = 0
for i in range(1, num):
    if num % i == 0:
        sum += i
if sum == num:
    print(f"{num} is a perfect number.")
else:
    print(f"{num} is not a perfect number.")
    
#Print smallest digit of a number.
num = int(input("Enter a number: "))
smallest = 9
while num > 0:
    digit = num % 10
    if digit < smallest:
        smallest = digit
    num //= 10
print("Smallest digit is:",smallest)

