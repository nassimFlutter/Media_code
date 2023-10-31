import numpy as np
# * create the array s
ar_0D = np.array(101)
ar_1D = np.array([1, 2, 3, 4, 5, 6, 4,])
ar_2D = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
ar_3D = np.array([[[1, 2, 3], [4, 5, 6]],
                  [[7, 8, 9], [10, 11, 12]],
                  [[13, 14, 15], [16, 17, 18]]])
# * print the arrays
print("2D array : \n", ar_2D)
#! -----------------------------------
# * print the dimensions the arrays
# ! use the ndim function
print("The dimension of this array : \n", ar_0D.ndim)
#!----------------------------------
# * You can set a a dimensions when create the arrays
# * An array can have any number of dimensions.
# *When the array is created, you can define the number of dimensions by using the (ndmin) argument.
arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print(arr.dtype)
print('number of dimensions :', arr.ndim)
# * covert the array to type
newarray = ar_1D.astype('S')
# * this copy of the array
x=newarray.copy()
print("this the copy " , x)
