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

# random decimal numbers between 0 to 1
# np.random.rand(shape)
# shape with three numbers (3,2,4) means 1 large array made up of 3 smaller arrays that are 2 by 4

# random integer numbers
# np.random.randint(startnumber, endnumber, size = (3,3))

# to repeat an arrays
# np.repeat(array, # of times, axis = 0 or 1)
# axis = 0 means array will be repeated as added rows, axis = 1 means added columns

# BE CAREFUL WHEN COPYING ARRAYS
# a = array
# b = a DOES NOT WORK, since b will reference a, so changes to b will also change a
# use .copy()
# b = a.copy() IS CORRECT

# array math
c = np.array([1,2,3,4])
# c + 2 adds 2 to all elements
# c - 2 subtracts 2 from all elements
# c * 2 multiplies 2 to all elements
# c / 2 divides 2 from all elements

# to do matrix multiplication (row size of one has to be the same as column size for other)
# use np.matmul(array, otherarray)
# np.matmul means matrix multiplication

# to create identity matrix, use np.identity(value)

# to find determinant of matrix, use np.linalg.det(arrayname)



# array statistics

# to find the min of array, use np.min(arrayname)
# can also use .min(arrayname, axis = 0 or 1) to find min of each column (0) or row (1)

# to find max of array, use np.max(arrayname)
# can also use axis argument here too

# to find sum of array, use np.sum(arrayname)
# can also use axis argument here too




# reorganizing arrays

# to change shape of array, use newarray = beforearray.reshape(new shape tuple)
# ex. afterarray = beforearray.reshape((8,1))
# beforearray values must be able to fit perfectly into the new shape, or there will be ERROR


# to vertically stack arrays, use np.vstack([array1, array2])
# np.vstack([array1, array2, array2, array2])

# to horizontally stack arrays, use np.hstack([array1, array2...])
# np.hstack([arary1, array2, array2, array2])




# to load data from file, use np.genfromtxt('file name.txt', delimeters = "whatever delimeter")
# ex. arrayname = np.genfromtxt('data.txt', delimters = ',')

# to change data type from text, use array.astype('data type here')
# ex. changeddatatype = arrayname.astype('int32')



# advanced indexing
# can pass a condition on an array
# ex. arrayname > 50 returns an array of True and Falses where <> 50

# to filter out values based on condition
# arrayname[arrayname > 50]
# when printed, will print out an array of only values greater than 50 in arrayname

# can index using a list
# a = np.array([1,2,3,4,5,6,7,8,9])
# a[[1,2,3]] will output array with items at 1,2,3 position --> [2,3,4]

# can index 2d arrays using multiple lists as well
# arrayname[[0,1,2,3], [1,2,3,4]] returns element at (row, column) --> (0,1), (1,2), (2,3), (3,4)

# can also pass a condition on an entire column or row using axis = 0 or 1
# axis = 0 means look vertically, axis = 1 means look horizontally.
# np.any(arrayname > 50, axis = 0)
# when printed, will look to see if any value in each column is greater than 50, then will print true or false.
# can also use np.all(condition, axis = 0 or 1) which looks if all values in a column meets condition, then prints true or false.

# Can also just straight up call conditions
# ((arrayname > 50) & (arrayname < 100)) returns an array of true and falses where arrayname meets these conditions.

# NOT IS NOT THE EXCLAMAITION POINT! It is the tilda ~.
# (~(arrayname > 50) & (arrayname < 100))
