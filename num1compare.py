#https://youtu.be/5rkKhsdJ0UU?list=PLlvFEn0NKwXIRHtvAhLrF7v1sDeNgL75g
import numpy as np
#compare list vs array
my_list = [1,2,3,4,5]
my_array = np.array([1,2,3,4,5])
print(my_list[0])
print(my_list[1])
print(my_array[0])
print(my_array[1])
#same output
print('='*50)
print(id(my_list[0]))
print(id(my_list[1]))
print(id(my_array[0]))
print(id(my_array[1]))
# output memory locations
#-elements of list are not in the same location
# 4469829344
# 4469829376
#-elements of array are  int he same location
# 4461866832
# 4461866832
my_list_of_data =[1, 2, "a", "b", True, 10.50]
my_array_of_data =np.array([1, 2, "a", "b", True, 10.50])
my_list_of_data_two =[1, 2, "a", "b", True, 10.50]
my_array_of_data_two =np.array([1, 2])
my_array_of_data_three =np.array([1, 2,10.9])
my_array_of_data_four =np.array([1, 2,10.9,"a"])
print("*"*50)
print(my_list_of_data)
#output [1, 2, 'a', 'b', True, 10.5]
print(my_array_of_data)# elements of array considered as strings while list are not
#output ['1' '2' 'a' 'b' 'True' '10.5']
print("*"*50)
print(type(my_list_of_data[0]))
#<class 'int'>
print(type(my_array_of_data[0]))
#<class 'numpy.str_'>
print("*"*50)
print(my_list_of_data_two)
print(my_array_of_data_two)
print("*"*50)
print(type(my_list_of_data_two[0]))
#<class 'int'>
print(type(my_array_of_data_two[0]))
#<class 'numpy.int64'>
print(type(my_array_of_data_three[0]))
#<class 'numpy.float64'>
my_array_of_data_four =np.array([1, 2,10.9,"a"])
print(type(my_array_of_data_four[0]))
#<class 'numpy.str_'>


