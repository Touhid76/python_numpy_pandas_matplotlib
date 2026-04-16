import numpy as np

data = np.array([50, 60, 70, 80, 90])

print("Average:", np.mean(data))
print("Max:", np.max(data))
print("Students > 75:", data[data > 75])

arr = np.array([[1,2,3],[4,5,6]])

np.sum(arr, axis=0)  # column sum
np.sum(arr, axis=1)  # row sum

arr = np.array([1,2,2,3,3,3])

print(np.unique(arr))