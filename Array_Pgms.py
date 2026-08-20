                                                                #ARRAY PROBLEMS

#APPEND()

'''
from array import array

arr = array('f', [10.5, 20.5, 30.5])

arr.append(40.5)

print(arr)

'''

#buffer_info()

'''
from array import array

arr = array('i', [10, 20, 30, 40])

print(arr.buffer_info())

'''

#byteswap()

'''
from array import array

arr = array('h', [10, 20, 30])

arr.byteswap()

print(arr)
'''


#count()

'''
from array import array

arr = array('i', [10, 20, 10, 30, 10])

print(arr.count(10))
'''

#extend()

'''
from array import array

a = array('d', [10.5, 20.5])
b = array('d', [50.5, 40.5])

a.extend(b)

print(a)
'''

#frombytes()

'''
from array import array

arr = array('b', [10, 20, 30])

data = arr.tobytes()

b = array('b')

b.frombytes(data)

print(b)
'''

#fromfile()
'''
from array import array

a = array('i', [10, 20, 30])

with open("data.bin", "wb") as f:
    a.tofile(f)

b = array('i')

with open("data.bin", "rb") as f:
    b.fromfile(f, 3)

print(b)
'''

#fromlist()

'''
from array import array

a = array('H')

a.fromlist([10, 20, 30, 40])

print(a)
'''

#fromunicode()
'''
from array import array

a = array('u')

a.fromunicode("HELLO")

print(a)
'''

#index()
'''
from array import array

a = array('l', [100, 200, 300, 400])

print(a.index(300))
'''

#insert()
'''
from array import array

a = array('f', [10.5, 20.5, 30.5])

a.insert(1, 15.5)

print(a)
'''

#pop()

'''
from array import array

a = array('q', [100000, 200000, 300000])

x = a.pop()

print("Removed:", x)
print(a)
'''

#remove()
'''
from array import array

a = array('I', [10, 20, 30, 40])

a.remove(20)

print(a)
'''

#reverse()
'''
from array import array

a = array('d', [10.5, 20.5, 30.5, 40.5])

a.reverse()

print(a)
'''

#tobytes()
'''
from array import array

a = array('h', [10, 20, 30])

data = a.tobytes()

print(data)
'''

#tofile()
'''
from array import array

a = array('i', [10, 20, 30, 40])

with open("data.bin", "wb") as f:
    a.tofile(f)

print("Data written successfully")
'''

#tolist()
'''
from array import array

a = array('f', [10.5, 20.5, 30.5])

b = a.tolist()

print(b)
'''


#tounicode()
'''
from array import array

a = array('u', 'PYTHON')

print(a.tounicode())
'''
