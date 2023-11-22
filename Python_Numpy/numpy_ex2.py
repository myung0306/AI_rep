import numpy as np

print("배열 Copy : 새로운 복사본 생성")
arr1=np.array([1, 2, 3, 4, 5])
arr2=arr1.copy()
print(arr2)

arr2[0]=100
print(arr1)
print(arr2)

arr1=np.array([[1, 2, 3], [4, 5, 6]])
arr2=arr1.copy()
print(arr2)

arr2[0, 0]=100
print(arr1)
print(arr2)

arr1=np.array([1, 2, 3, 4, 5])
arr2=arr1.copy()
arr2[0]=100
print(arr1.base)
print(arr2.base)
print("\n")

print("배열 View : 기존 array의 다른 보기를 생성")
arr1=np.array([1, 2, 3, 4, 5])
arr2=arr1.view()
arr2[0]=100

print(arr1)
print(arr2)
print(arr1.base)
print(arr2.base)

arr1=np.array([1, 2, 3, 4, 5])
arr2=arr1.view()
print(arr1)
print(arr2)
arr2.dtype=np.int8
arr1[0]=10
print(arr1)
print(arr2)

arr1=np.array([1, 2, 3, 4, 5])
arr2=arr1.view()
arr2.dtype=np.int16
arr1[0]=10
print(arr1)
print(arr2)

arr1=np.array([1, 2, 3, 4, 5, 6])
arr2=arr1.view().reshape(2, 3)
arr1[0]=10
print(arr1)
print(arr2)

arr1=np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(arr1.shape)
arr1=np.array([[1, 2, 3], [4, 5, 6]])
print(arr1.shape)
arr1=np.array([[[1, 2, 3], [4, 5, 6]],[[7, 8, 9], [10, 11, 12]]])
print(arr1.shape)
print("\n")

print("배열 형태 변경")
arr1=np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
arr2=arr1.reshape(3, 4)
arr3=arr1.reshape(2, 2, 3)

print(arr1)
print(arr2)
print(arr3)

arr1=np.array(list(range(10)))
print(arr1, arr1.dtype)

arr1=np.array(range(10))
print(arr1, arr1.dtype)
print("\n")

print("reshape은 view를 생성")
arr1=np.array(list(range(1, 13)))
arr2=arr1.reshape(3, 4)
arr3=arr1.reshape(2, 2, 3)
arr1[0]=16
print(arr1.base)
print(arr2.base)
print(arr3.base)
print("\n")

print("차원의 길이에 -1을 주면 자동으로 길이를 결정")
arr1=np.array(list(range(1, 13)))
arr2=arr1.reshape(-1, 4)
arr3=arr1.reshape(2, 2, -1)
print(arr1)
print(arr2)
print("\n")


arr1=np.array(list(range(1, 10)))
for i in arr1:
    print(i)
    
arr2=np.array([[1, 2, 3], [4, 5, 6]])
for i in arr2:
    print(i)
        
arr2=np.array([[1, 2, 3], [4, 5, 6]])
for i in arr2:
    for j in i:
        print(j)
        
arr3=np.array([[[1, 2, 3], [4, 5, 6]],[[7, 8, 9], [10, 11, 12]]])
for i in arr3:
    print(i)

for i in arr3:
    for j in i:
        print(j)

for i in arr3:
    for j in i:
        for k in j:
            print(k)
            
#다차원 배열의 항목을 순차적으로 처리
arr1=np.array(range(1, 7))

for idx, i in np.ndenumerate(arr1):
    print(idx, i)
    
for idx, i in np.ndenumerate(arr2):
    print(idx, i)

arr3=np.array([[[1, 2, 3], [4, 5, 6]],[[7, 8, 9], [10, 11, 12]]])
for idx, i in np.ndenumerate(arr3):
    print(idx, i)

#Mission
arr1=np.array(list(range(24)))
print(arr1.shape)

arr2=arr1.reshape(4, 6)
print(arr2.shape)

arr3=arr1.reshape(2, 3, 4)
print(arr3.shape)


        

