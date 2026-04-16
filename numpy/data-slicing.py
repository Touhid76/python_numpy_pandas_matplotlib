import numpy as np
arr = np.array([10,20,30,40,50])

print(arr[1])      # 20
print(arr[1:4])    # [20 30 40]
print(arr[:3])     # [10 20 30]


#2d array
arr = np.array([[1,2,3],[4,5,6]])

print(arr[0,1])    # 2
print(arr[:,1])    # column