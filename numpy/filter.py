import numpy as np
a=[12,3,4,5,6,7]
print(a)
filtered=[]
for i in a:
    if(i%2==0):
        filtered.append(i)

filtered=np.sort(filtered)
print(filtered)