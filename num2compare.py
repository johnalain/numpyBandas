#----------------------------
#numpy => compare performance and memory usage
#----------------------------
#https://youtu.be/koMDndoAvCc
import numpy as np
import time 
import sys
elements = 150
my_list1 = range(0, elements)# we can't put start 0 cuz 0 is the default
my_list2 = range( elements)
for n in range(elements):
    print(n)
print('################################')
#output 0 .........149

my_array1 = np.arange(elements)
my_array2 = np.arange(elements)
# for n1,n2 in zip(my_list1,my_list2):
#     print(n1+n2)#output 0 ......249
list_start = time.time()
list_result = [(n1,n2) for n1,n2 in zip(my_list1,my_list2)]
print(f"list time: {time.time()-list_start}")
array_start = time.time()
print(f"array time: {time.time()-array_start}")
# array_result = my_array1 + my_array2
print('#'*20) 
# print(list_result) 
# print(array_result) 
#list time: 0.0002009868621826172
# array time: 9.5367431640625e-07 
