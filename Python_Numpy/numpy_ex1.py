import numpy as np

print(np.__version__)

#배열(1D)
arr1=np.array([1, 2, 3, 4, 5])
print(arr1, arr1.ndim, type(arr1))

#배열(2D)
arr2=np.array([[1, 2, 3], [4, 5, 6]])
print(arr2, arr2.ndim, type(arr1))

#배열(3D)
arr3=np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]]])
print(arr3, arr3.ndim, type(arr1))

#배열(1D) index
arr=np.array([1, 2, 3, 4, 5])
print(arr[0])
print(arr[2])
print(arr[0]+arr[2])
print(arr[-1])

#배열(2D) index
arr=np.array([[1, 2, 3], [4, 5, 6]])
print(arr[0])
print(arr[0][1])
print(arr[0, 1])
print(arr[-1])

#배열(3D) index
arr=np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr[0])
print(arr[0, 1])
print(arr[0, 1, 2])
print(arr[-1])

#배열(1D) Slicing
arr=np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(arr[4:6])
print(arr[4:])
print(arr[:6])
print(arr[-5:-3])
print(arr[-5:])
print(arr[:-3])

#배열(2D) Slicing
arr=np.array([[1, 2, 3], [4, 5, 6]])
print(arr[1:])
print(arr[1, 1:])
print(arr[1:, 1:])
print(arr[:1, 0])

#배열(3D) Slicing
arr=np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr[1:])
print(arr[1:, 1:])
print(arr[1:, 1:, :2])
print(arr[:1, 1, :2])

#배열 Type : int8, int16, int32, int64 등은 int형
arr=np.array([1, 2, 3, 4, 5])
print(arr.dtype)
arr=np.array([1, 2, 3, 4, 5], dtype=np.int8)
print(arr.dtype)
arr=np.array([1, 2, 3, 4, 5], dtype=np.int32)
print(arr.dtype)
arr=np.array([1, 2, 3, 4, 5], dtype=np.int64)
print(arr.dtype)
arr=np.array([1, 2, 3, 4, 5], dtype=np.int_)
print(arr.dtype)

#배열 Type : uint8, uint16, uint32, uint64 등은 unsigned int형
arr=np.array([1, 2, 3, 4, 5], dtype=np.uint8) 
print(arr.dtype)
arr=np.array([1, 2, 3, 4, 5], dtype=np.uint32)
print(arr.dtype)
arr=np.array([1, 2, 3, 4, 5], dtype=np.uint64)
print(arr.dtype)

#배열 Type : float16, float32, float64
arr=np.array([1.0, 2.0, 3.0, 4.0, 5.0])
print(arr.dtype)
arr=np.array([1.0, 2.0, 3.0, 4.0, 5.0], dtype=np.float16)
print(arr.dtype)
arr=np.array([1.0, 2.0, 3.0, 4.0, 5.0], dtype=np.float32)
print(arr.dtype)
arr=np.array([1.0, 2.0, 3.0, 4.0, 5.0], dtype=np.float64)
print(arr.dtype)
arr=np.array([1.0, 2.0, 3.0, 4.0, 5.0], dtype=np.float_)
print(arr.dtype)

#배열 Type : boolean
arr=np.array([1, 2, 0, 4, 0], dtype=np.bool_)
print(arr)
print(arr.dtype)

#배열 Type : string, unicode
arr=np.array(['11', '12'])
print(arr.dtype)

arr=np.array(['1', '2'], dtype=np.string_)
print(arr.dtype)

arr=np.array(['1', '대한민국'], dtype=np.unicode_)
print(arr)
print(arr.dtype)
