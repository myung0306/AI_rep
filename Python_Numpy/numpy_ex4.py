import numpy as np

#array Stack
arr1=np.array([1, 2, 3, 4])
arr2=np.array([5, 6, 7, 8])

arr3=np.stack((arr1, arr2))
print(arr3)

arr3=np.stack((arr1, arr2), axis=0)
print(arr3)

arr3=np.stack((arr1, arr2), axis=1)
print(arr3)

arr1=np.array([[1, 2], [3, 4]])
arr2=np.array([[5, 6], [7, 8]])

arr3=np.stack((arr1, arr2))
print(arr3)

arr4=np.stack((arr1, arr2), axis=0)
print(arr4)

arr1=np.array([[1, 2], [3, 4]])
arr2=np.array([[5, 6], [7, 8]])

arr3=np.stack((arr1, arr2), axis=1)
print(arr3)

arr4=np.stack((arr1, arr2), axis=2)
print(arr4)

arr1=np.array([1, 2, 3, 4])
arr2=np.array([5, 6, 7, 8])

arr3=np.hstack((arr1, arr2))
print(arr3)

arr4=np.vstack((arr1, arr2))
print(arr4)

arr5=np.dstack((arr1, arr2))
print(arr5)

arr1=np.array(list(range(1, 10)))
print(np.array_split(arr1, 4))

arr1=np.array(list(range(1, 10)))
arr2=np.array_split(arr1, 3)
print(arr2)
print(arr2[0])
print(arr2[1])
print(arr2[2])

