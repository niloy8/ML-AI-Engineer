#So NumPy solves:

#Fast numerical computation using arrays.

import numpy as np
arr = np.array([1,2,3])
print(arr)

matrix = np.array([[1,2,3],
                   [4,5,6]])
print(matrix)

tensor = np.array([[[1,2],[3,4]],
                   [[5,6],[7,8]]])

print(tensor.shape)

print(tensor.ndim)

arr = np.array([10,20,30,40])



print(arr[0])      # 10
print(arr[1:4])

print(matrix[0,2])
a = np.array([1,2,3])
b = np.array([4,5,6])

print(a + b)

#Broadcasting

arr = np.array([1,2,3])
print(arr+10)


#Aggregation Functions
arr = np.array([10,20,30])

print(np.mean(arr))
print(np.sum(arr))
print(np.max(arr))
print(np.std(arr))


#Grade Calculator
grades = np.array([
    [85, 90, 78, 92],
    [88, 76, 95, 89],
    [70, 80, 65, 75]
])

student_avg = np.mean(grades, axis=1)
print(student_avg)

subject_avg = np.mean(grades, axis=0)

print(subject_avg)

#.reshape() → Change the shape
arr = np.array([1,2,3,4,5,6])
print(np.shape(arr))
new_arr = arr.reshape(3,2)
new_arr = arr.reshape(2, -1)
# print(new_arr)

#.flatten() → Make everything 1D

#Turns multi-dimensional array into a single row.
arr = np.array([[1,2],[3,4]])

a = arr.flatten()
b = arr.ravel()

a[0] = 100
b[1] = 200

print(arr)

print(np.random.rand(3))

print(np.random.rand(2,3))

print(np.random.randint(0, 10, size=5))

#Splitting Dataset
# indices = np.random.permutation(len(data))

np.random.seed(42)

print(np.random.rand(3))


#np.dot(a, b) → Dot Product
a = np.array([1,2,3])
b = np.array([4,5,6])

print(np.dot(a, b))

#Matrix Multiplication
A = np.array([[1,2],
              [3,4]])

B = np.array([[5,6],
              [7,8]])

print(A @ B)
# Transpose → A.T

# Transpose swaps rows and columns.