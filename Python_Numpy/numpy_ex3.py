import numpy as np

#concatenate : 여러 배열을 합쳐서 하나의 배열로 만듦
arr1=np.array([1, 2, 3, 4])
arr2=np.array([5, 6, 7, 8])

arr3=np.concatenate((arr1, arr2))

print(arr3)

arr1=np.array([[1, 2], [3, 4]])
arr2=np.array([[5, 6], [7, 8]])

arr3=np.concatenate((arr1, arr2))
print(arr3)

arr4=np.concatenate((arr1, arr2), axis=0)
print(arr4)

arr5=np.concatenate((arr1, arr2), axis=1)
print(arr5)

arr1=np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
arr2=np.array([[[9, 10], [11, 12]], [[13, 14], [15, 16]]])

arr3=np.concatenate((arr1, arr2))
print(arr3)

arr4=np.concatenate((arr1, arr2), axis=0)
print(arr4)

arr5=np.concatenate((arr1, arr2), axis=1)
print(arr5)

arr6=np.concatenate((arr1, arr2), axis=2)
print(arr6)