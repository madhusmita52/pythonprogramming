#CREATE A 1D ARRAY WITH VALUES 0 TO 9
import numpy as np
arr=np.arange(10)
print(arr)
#CREATE A 1D ARRAY OF ZEROS
import numpy as np
num=np.zeros(5,int)
print(num)
#CREATE A 1D ARRAY OF ONES
import numpy as np
num=np.ones(6,int)
print(num)
#CREATE A 1D ARRAY WITH RANDOM INTEGERS
from numpy import random
x = random.randint(3, 9)
print(x)
#CREATE 2D ARRAY OF SHAPE (3,3)WITH VALUES 0 TO 8
arr=np.arange(9).reshape(3,3)
print(arr)
#CREATE 3*3 ARRAY FILLED WITH ZEROS
arr=np.zeros((3,3),int)
print(arr)
#CREATE 3*3 ARRAY FILLED WITH ONES
arr=np.ones((3,3),int)
print(arr)
#CREATE A 3*3 IDENTITY MATRIX
arr=np.eye(3)
print(arr)
#CREATE A ARRAY OF FIVES
arr=np.full(10,5)
print(arr)
#CREATE AN ARRAY OF 10 RANDOM INTEGERS BETWEEN 1 AND 50
#CREATE A 1D ARRAY OF 10 EVENLY SPACED VALUES BETWEEN 0 TO 1
arr=np.linspace(0,1,10)
print(arr)
#CHECK THE SHAPE OF A NUMPY ARRAY
arr=np.arange(12).reshape(3,4)
print(arr.shape)
#ACCESS THE FIRST ELEMENT OF AN ARRAY
arr=np.array([10,20,30,40])
print(arr[0])
#SLICE THE FIRST 3 ELEMENT OF AN ARRAY
arr=np.array([10,20,30,40])
print(arr[:3])
#SLICE THE LAST 2 ELEMENTS OF AN ARRAY
arr=np.array([10,20,30,40])
print(arr[-2:])
#REVERSE A NUMPY ARRAY
arr=np.array([10,20,30,40])
print(arr[::-1])
#ACCESS THE ELEMENT AT RO=1, COL=2 IN A 2D ARRAY
arr=np.arange(9).reshape(3,3)
print(arr[1,2])
#SELECT THE FIRST ROW OF 2D ARRAY
arr=np.arange(9).reshape(3,3)
print(arr[0])
#SELECT THE FIRST COLUMN OF A 2D ARRAY
arr=np.arange(9).reshape(3,3)
print(arr[:0])
#ADD TWO ARRAYS ELEMENT WISE
a=np.array([1,2,3])
b=np.array([4,5,6])
print(a+b)
#SUBSTRACT TWO ARRAY
a=np.array([1,2,3])
b=np.array([4,5,6])
print(a-b)
#MULTIPLY TWO ARRAY
a=np.array([1,2,3])
b=np.array([4,5,6])
print(a*b)
#DIVIDE TWO ARRAYS ELEMENT-WISE
a=np.array([1,2,3])
b=np.array([4,5,6])
print(a/b)
#SQUARE EACH ELEMENT
a=np.array([1,2,3])
print(a**2)
#FIND THE SUM OF ALL ELEMENTS
arr=np.array([1,2,3,4,5])
print(arr.sum())
#FIND THE MEAN OF ELEMENTS
arr=np.array([1,2,3,4,5])
print(arr.mean())
#FIND THE Maximum OF ELEMENTS
arr=np.array([1,2,3,4,5])
print(arr.max())
#SUM ALONG ROWS OF 2D ARRAY
arr=np.arange(9).reshape(3,3)
print(arr.sum(axis=1))
#SUM ALONG COLUMNS OF 2D ARRAY
arr=np.arange(9).reshape(3,3)
print(arr.sum(axis=0))
#FIND THE STANDARD DEVIATION
arr=np.array([1,2,3,4,5])
print(arr.std())
#FIND THE VARIANCE
arr=np.array([1,2,3,4,5])
print(arr.var())
#FIND THE INDEX OF MAXIMUM ELEMENT
arr=np.array([1,2,3,4,5])
print(arr.argmax())
