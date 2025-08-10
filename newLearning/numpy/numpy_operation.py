# Numpy : it is a fundamental package for scientific computing in Python. It provides the support for the large,
# multi-dimensional arrays and matrices, along with a collection of mathematical functions to operate on these arrays.
#Majorly used for mathematical and logical operations on arrays.
import numpy as np

#1D array
# arr1=np.array([1,2,3,4,5])  
# print(arr1)  
# print(type(arr1))  #it will give the type of the array
# print(arr1.shape)   #it will give the shape of the array


#two dimensional array
# arr2=np.array([1,2,4,5,6])
# arr2=arr2.reshape(1,5)  #it will reshape the array into 1*5 matrix and will have 2 closing brackets
# print(arr2)  #it will give the reshaped array 

# arr3=np.array([[1,2,3],[4,5,6]])  #it will create a 2*3 matrix
# print(arr3)  
# print(arr3.shape)   #it will give the shape of the array

# arr4=np.arange(0,10,3).reshape(4,1)
# print(arr4)  #it will give the array from 0 to 10 with step of 3

# #Inbuilt functions
# print(np.ones((2,3)))  #it will create a 2*3 matrix with all ones


# #Identity Matrix
# print(np.eye(4))  #it will create a 4*4 identity matrix



#Numpy vactorized operation
# arr1=np.array([1,2,3,4,5])
# arr2=np.array([6,7,8,9,10])
# print (arr1+arr2)  #it will add the two arrays element wise
# print (arr1-arr2)  #it will subtract the two arrays element wise
# print (arr1*arr2)  #it will multiply the two arrays element wise
# print (arr1/arr2)  #it will divide the two arrays element wise
 
# print (arr1**2)  #it will square the two arrays element wise


# #Universal functions
# arr1=np.array([1,2,3,5])
# print(np.sqrt(arr1))  #it will give the square root of the array element wise
# print(np.exp(arr1))  #it will give the exponential of the array element wise
# print(np.log(arr1))  #it will give the logarithm of the array element wise
# print(np.sin(arr1))  #it will give the sine of the array element wise
# print(np.cos(arr1))  #it will give the cosine of the array element wise
# print(np.tan(arr1))  #it will give the tangent of the array element wise


#array slicing and filtering the values in the 2Dmatrix
# arr1=np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]])
# print(arr1[0:2,0:2])  #it will give the first two rows and first two columns of the array
# print(arr1[0][1])
# print(arr1[1][1],arr1[1][2],arr1[2][0],arr1[2][1],arr1[2][2])  #it will give the second row and second column of the array
# print(arr1[0:,2])  #it will give the second column of the array
# print(arr1[1:,1:3])

# #Modify the matrix
# arr1[0,0]=69  #it will modify the first element of the array
# print(arr1)  #it will give the modified array

#Normalization of the array: its basically making the values between 0 and 1 as mean 0 and standard deviation 1
data=[1,2,3,4,5,6,7,8,9,10]
mean=np.mean(data)  #it will give the mean of the array
print(mean)
std_mean=np.std(data)  #it will give the standard deviation of the array
print(std_mean)
#Normalization
normalized_data=(data-mean)/std_mean  #it will give the normalized data
print(normalized_data)  #it will give the normalized data

#Median:
median=np.median(data)  #it will give the median of the array
print(median)  #it will give the median of the array
#Mode:
mode=np.argmax(np.bincount(data))  #it will give the mode of the array
print(mode)  #it will give the mode of the array
#Variance:
variance=np.var(data)  #it will give the variance of the array
print(variance)  #it will give the variance of the array

#Logical operations:
data=np.array([[[1,2,3,4,5,6,7,8,9,10],[11,12,13,14,15,16,17,18,19,20],[21,22,23,24,25,26,27,28,29,30],[31,32,33,34,35,36,37,38,39,40]]])
print(data>5)  #it will give the boolean array of the values greater than 5
print(data[(data>5) & (data<10)] )  #it will give the values greater than 5 in the array and less than 10
