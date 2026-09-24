
                                                            
                                                                        #NUMPY...


#BASICS
'''
import numpy
print(numpy.__version__)

'''


'''
import numpy as np

a = np.array(10)
b = np.array(5)

print("Addition:",(a+b))
print("Subtraction:",(a-b))
print("Multiplication:",(a*b))
print("Division:",(a/b))
print("Floor Division:",(a//b))
print("Modulus:",(a%b))
print("Power:",(a**b))

'''

#Codes
# program  1
'''
import numpy as np
a=np.array([10,11,12,13,14,15,16,33,23,45])
print("Array:",a)
print("Array size:",a.size)
print("Data Type:",a.dtype)
print("Dimension:",a.ndim)
'''


# program  2
'''
import numpy as np

a = np.array(10)
b = np.array(5)

print("Addition:",(a+b))
print("Subtraction:",(a-b))
print("Multiplication:",(a*b))
print("Division:",(a/b))
print("Modulus:",(a%b))
'''

# program  3

'''
import numpy as np

a=np.array([10,11,12,13,14,15,16,33,23,45])
print("Sum:",sum(a))
print("minimum no.:",min(a))
print("max no.:",max(a))
print("average:",np.mean(a))

'''

# program  4

'''
import numpy as np
a=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])

even=a[a%2==0]
odd=a[a%2!=0]

print("Even no. :",even)
print("odd no. :",odd)


'''

# program  5

'''
import numpy as np
a=np.array([1,2,3,4,5,6,7,8,9,10,11,12])

print("2 X 6 matrix:",a.reshape(2,6))
print("3 X 4 matrix:",a.reshape(3,4))
print("4 X 3 matrix:",a.reshape(4,3))
'''
# program  6

'''
import numpy as np

a = np.array([[1,2,3],
              [4,5,6],
              [7,8,8]])

b = np.array([[9,3,7],
              [3,5,6],
              [3,2,1]])

print("Matrix Addition:")
print(np.add(a,b))
'''

# program  7
'''
import numpy as np

a = np.array([[1,2],
              [3,4]])

b = np.array([[5,6],
              [7,8]])

print("Matrix multiplication:")
print(np.matmul(a,b))
'''

# program  8
'''
import numpy as np

a = np.array([[1,2,3,4],
              [5,6,7,8],
              [9,10,11,12]])

print("Original Matrix:")
print(a)

print("Transpose:")
print(a.T)
'''

# program  9
'''
import numpy as np

a = np.array([[1,2,3,4],
              [5,6,7,8],
              [9,10,11,12],
              [13,14,15,16]])

print("First row:", a[0])
print("last column:", a[:,3])
print("diagonal:", np.diag(a))
print("second and third rows:")
print(a[1:3])
'''

# program  10
'''
import numpy as np

a = np.array([[1,2,3,4],
              [5,6,7,8],
              [9,10,11,12],
              [13,14,15,16]])

print("Sum of each row:", np.sum(a, axis=1))
print("Sum of each column:", np.sum(a, axis=0))
'''

# program  11
'''
import numpy as np

a = np.arange(1,21)

print("First 5:", a[:5])
print("Last 5:", a[-5:])
print("Alternate:", a[::2])
print("Reverse:", a[::-1])
'''
# program  12
'''
import numpy as np

a = np.array([10,25,60,45,75,30,90,20,55,40])

a[a > 50] = 0

print("Array:", a)
'''

# program  13
'''
import numpy as np

a = np.array([50,20,80,10,60,30])

print("Ascending:", np.sort(a))
print("Descending:", np.sort(a)[::-1])
'''

# program  14
'''
import numpy as np

a = np.array([10,20,10,30,20,40,30,50])

print("Unique elements:", np.unique(a))
'''

# program  15
'''
import numpy as np

a = np.array([[1,2],
              [3,4]])

b = np.array([[5,6],
              [7,8]])

print("Horizontal:")
print(np.hstack((a,b)))

print("Vertical:")
print(np.vstack((a,b)))
'''
# program  16

'''
import numpy as np

marks = np.array([75,80,65,90,85,70,95,60,88,78])

print("highest:", np.max(marks))
print("lowest:", np.min(marks))
print("Average:", np.mean(marks))
print("median:", np.median(marks))
print("standard Deviation:", np.std(marks))
'''

# program  17
'''
import numpy as np

marks = np.array([45,67,89,56,78,92,34,75,81,60,
                  88,72,55,95,63,70,48,85,90,52])

average = np.mean(marks)

print("Class Average:", average)
print("Above Average:", marks[marks > average])
'''

# program  18
'''
import numpy as np

a = np.arange(1,25).reshape(2,3,4)

print("Array:")
print(a)

print("Dimensions:", a.ndim)
print("Shape:", a.shape)
print("Size:", a.size)
'''

# program  19
'''
import numpy as np

a = np.arange(1,25).reshape(2,3,4)

print("First element:", a[0,0,0])
print("Last element:", a[1,2,3])
print("Element [0,1,2]:", a[0,1,2])
print("Element [1,2,3]:", a[1,2,3])
'''

# program  20
'''
import numpy as np

a = np.arange(1,25).reshape(2,3,4)

print("Total Sum:", np.sum(a))

print("Sum of each layer:")
print(np.sum(a, axis=(1,2)))

print("Sum along rows:")
print(np.sum(a, axis=2))

print("Sum along columns:")
print(np.sum(a, axis=1))
'''


# program  21
'''
import numpy as np

a = np.random.randint(1,101,size=(2,3,4))

print("Original Array:")
print(a)

a[a > 50] = 0

print("After replacing:")
print(a)
'''

# program  22
'''
import numpy as np

a = np.random.randint(1,101,size=(3,4,5))

print("Array:")
print(a)

print("Mean:", np.mean(a))
print("median:", np.median(a))
print("Standard Deviation:", np.std(a))
print("variance:", np.var(a))
print("minimum:", np.min(a))
print("maximum:", np.max(a))
'''
# program  23
'''
import numpy as np

a = np.arange(1,25).reshape(2,3,4)

print("Original Array:")
print(a)

b = a.flatten()

print("Flattened Array:")
print(b)
'''

# program  24
'''
import numpy as np

a = np.arange(1,28).reshape(3,3,3)

b = a.flatten()

print("Flattened Array:", b)
print("Sum:", np.sum(b))
print("Average:", np.mean(b))
print("Maximum:", np.max(b))
print("Minimum:", np.min(b))
'''

# program  25
'''
import numpy as np

a = np.random.randint(1,101,size=(3,4,5))

b = a.flatten()

average = np.mean(b)

print("Array:")
print(a)

print("Greater than 50:")
print(b[b > 50])

print("Even numbers:")
print(b[b % 2 == 0])

print("Less than average:")
print(b[b < average])
'''
