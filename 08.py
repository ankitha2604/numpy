#creating numpy array
import numpy 
arr=numpy.array([1,2,3,4,5])
print(arr)

#convert 1-D array to 2-D array
import numpy as np
arr=np.array([3,5,7,9,1,15,18,22])
print(arr)
arr1=(arr[1:6])
print(arr1)
arr2=arr.reshape(4,2)
print("convert 1-D array to 2-D array")
print("2D array is:",arr2)

#Slicing 3rd value to end
import numpy as np
arr=np.array([3,5,8,9,11,19,22,25,27])
print("Slice starting from 3rd value to end")
print(arr[0:5])

#Slice 0 to 4 index
import numpy as np
arr=np.array([1,2,3,4,5,6,8,9])
print("Slice 0 to 4 index are:",arr[::4]) 
