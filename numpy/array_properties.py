import numpy as np
# array declaration
a = np.array([1, 2, 3], np.int64)
b = np.array([[1, 2], [3, 4]], np.float64)

print(a.shape)   # (3,)
print(b.shape)   # (2,2)
print(a.ndim)    # dimension
print(a.dtype)   # data type