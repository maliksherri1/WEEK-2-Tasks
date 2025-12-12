#  Name Malik Sherdil
# WEEK 2 TASKS
# NUMPY 
# Numpy creation of arrays

import numpy as np
# 1D array
# a = np.array([1, 2, 3])

# # 2D array
# b = np.array([[1, 2, 3], [4, 5, 6]])

# # zero array
# c = np.zeros((2, 3))

# # ones array
# d = np.ones((2, 3))

# # Range of values
# e = np.arange(0,10,1)

# # liner space
# f = np.linspace(0,1,5)

# #  ARRAY INDEXING AND SLICING
# arr = np.array([[1, 2, 3, 4, 5],
#                 [6, 7, 8, 9, 10],
#                 [11, 12, 13, 14, 15]])

# # print(arr[1, 2]) 
# # print(arr[1:2]) 


# # Mathematical operations
# x = np.array([[1, 2], [3, 4]])
# y = np.array([[5, 6], [7, 8]])

# # Addition
# add = np.add(x, y)
# # Subtraction
# sub = np.subtract(x, y)
# # Multiplication
# mul = np.multiply(x, y)
# # Division
# div = np.divide(x, y)

# # Aggregation
# arr = np.array([1, 2, 3, 4, 5])
# # print(arr.sum())      
# # print(arr.mean())      
# # print(arr.std())       
# # print(arr.min())
# # print(arr.max())      

# # RESHAPING ARRAYS
# arr = np.arange(1, 13)
# ra = arr.reshape((3, 4))
# # print(ra)

# # Matrix operations
# A = np.array([[1, 2], [3, 4]])
# B = np.array([[5, 6], [7, 8]])

# # Matrix multiplication
# print(A.dot(B))

# # addition
# print(A + B)

# # Transpose
# print(A.T)

# # Inverse
# print(np.linalg.inv(A))

# Broadcasting

# a = np.array([[1, 2, 3],
#               [4, 5, 6],
#               [7, 8, 9]])   
# # print(a + 10)  


# # Random numbers generation
# rand_arr = np.random.rand(3, 3)
# print(rand_arr)