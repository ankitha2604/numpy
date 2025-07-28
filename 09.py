#use Slicing a 2-D array
import numpy as np
arr=np.array([[3,5,7,9],[11,15,18,22]])
print("Use Slicing a 2-D array")
print("Slicing with 2-D array is:",arr[1,1:3])

#Slicing 3D array
import numpy as np
arr=np.array([[[3,5,7,9],[11,15,18,22]],
              [[1,2,3,4],[5,6,7,8]]])
print("Slicing 3D array")
print("Slicing 3D array is:",arr[0,1,0:2])
