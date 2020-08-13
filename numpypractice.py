import numpy as np
import sys

# to initialize array
# a = np.array([1, 2, 3])
# b - np.array([[9.0, 8.0, 7.0], [6.0, 5.0, 4.0]])

# to get number of dimensions of an array, use .ndim (number of dimensions)
# a.ndim

# to get array shape (rows, columns), use .shape
# b.shape

# get data type of items in array, use .dtype
# a.dtype --> int64

# to specify data type of array, use dtype = 'whatever type'
# ex. a = np.array([1, 2, 3] dtype = 'int16')

# get size of each item in bytes using .itemsize
# a.itemsize

# get total size in bytets of array using .nbytes
# a.nbytes

# get length of array using .size
# a.size

a = np.array([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]])
# a.shape = (2,7)

# to get a specifc element, use [row, column]
# a[1,5] = 13
# a[1, -2] = 13

# to get a specific row, use [row, column]
# a[desired row, :]

# to get a specific column
# a[:, desired column]

# to have a start and end, use startindex:endindex:stepsize
# a[0, 1:6:2])
# looks at first row, 1st to 5th column (6 is not included), and uses a stepsize of 2

# to change element
# a[row, column] = desired value

# to change multiple elements
# a[:, 2] = 5
# changes all values in 2nd column to 5
# a[:, 2] = [1,2]
# changes all vaues in 2nd column to alternating 1, 2

# to create arrays
# all 0s matrix --> np.zeros((shape in coordinates))
# ex. np.zeros((2,2)), np.zeros(2)

# all 1s matrix --> np.ones((4,2,2))

# any other number, use np.full((shape in coordinates), desired value)
# ex. np.full((2,2), 99) returns a 2 by 2 array full of 99s.

# random decimal numbers
# np.random.rand(shape)
# shape with three numbers (3,2,4) means 1 large array made up of 3 smaller arrays that are 2 by 4
