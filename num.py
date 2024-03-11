#-------------------------
#numpy => create Arrays
from turtle import pd
import numpy as np
#print(dir(np))#print all functions of numpy
#https://youtu.be/vGJxavinB9M?list=PLlvFEn0NKwXIRHtvAhLrF7v1sDeNgL75g
#print(dir(pd))#print all functions of pandas
my_list = [1, 2, 3, 4, 5]
my_array = np.array(my_list)
print('*' *30)

print(type(my_list))#<class 'list'>
print(type(my_array))#output <class 'numpy.ndarray'> ndarray = nondimentional array
print('*' *30)

#accessing element
print(my_list[0])#output 1
print(my_array[0])#output 1 no difference btween two prints
print('*' *30)
a = np.array(10)
b = np.array([10, 20])
c = np.array([[1, 2], [3, 4]])
d = np.array([[[5,6],[7,9]],[[1,3],[4,6]]])#d[0]=[5,6],[7,9]||d[1]=[1,3],[4,6]
#d[0]=[5,6],[7,9] d[0][1]=[7,9] ,d[0][1][1]=9
print(d[1][1][1])#output 6
#same output
print(d[1, 1, 1])#output 6
print(d[1,1,0])#output 4
print('*' *30)
#number of dimensions
print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)
#output 0-1-2-3
print('*' *30)
# custom dimensions create 3 dimensional array
my_custom_array = np.array([1,2,3],ndmin=3)
print(my_custom_array)
print(my_custom_array.ndim)
#[[[1 2 3]]]
#3
print(my_custom_array[0][0][0])
#same result
print(my_custom_array[0,0,0])

print('*' *30)


