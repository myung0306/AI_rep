import numpy as np
import pandas as pd

print(pd.__version__)

data={
    "subject":["국어", "영어", "수학", "과학"],
    "score": [80, 70, 90, 95]
}

df=pd.DataFrame(data)
print(df)

#Series:1차원 배열의 자료구조로 같은 타입의 데이터로 구성 되어있음
#Index와 Value로 구성
arr1 = ["국어", "영어", "수학", "과학"]
ser1= pd.Series(arr1)

print(ser1)
print(ser1[0], ser1[1], ser1[2], ser1[3])
print("\n")

#Series생성 시에 index를 함께 지정해서 생성
#지정된 index로 Series값에 접근 가능
arr1=[80, 70, 90, 95]
idx1=["국어", "영어", "수학", "과학"]
ser1=pd.Series(arr1, index=idx1)

print(ser1)
print(ser1["국어"], ser1["영어"], ser1["수학"], ser1["과학"])

data={
    "국어" : 80,
    "영어" : 70,
    "수학" : 90,
    "과학" : 95
}
ser1=pd.Series(data)
print(ser1)
print(ser1["국어"], ser1["영어"], ser1["수학"], ser1["과학"])
print("\n")

#Index
#index, values를 이용해 index 및 values에 접근 가능
ser2=pd.Series(data, index=["국어", "수학"])
print(ser2)
print(ser2["국어"], ser2["수학"])
print(ser2.loc["국어"], ser2.loc["수학"])
print(ser2.iloc[0], ser2.iloc[1])
print(ser2.index)
print(ser2.values)
print("\n")

#Type
#문자는 object type
arr1=["국어", "영어", "수학", "과학"]
ser1=pd.Series(arr1)
print(ser1)
print(ser1.index)
print(ser1.values)
print("\n")

#숫자는 int, float type
arr2=[80, 70, 90, 95]
ser2=pd.Series(arr2)
print(ser2)
print("\n")

arr3=[0.8, 0.7, 0.9, 0.95]
ser3=pd.Series(arr3)
print(ser3)
print("\n")

arr4=["2023-09-04 18:30:00", "2023-09-04 19:30:00", "2023-09-04 20:30:00", "2023-09-04 21:30:00"]
ser4=pd.Series(arr4)
print(ser4)
print("\n")

#날짜는 to_datetime()명령으로 Datetime형식으로 변환
ser5=pd.to_datetime(ser4, format='%Y-%m-%d %H:%M:%S')
print(ser5)
print("\n")

#데이터가 정제되지 않는 경우는 object형
arr5=[1, 2, 3, "영어"]
ser5=pd.Series(arr5)
print(ser5)
print("\n")

#astype() 명령으로 형식으로 변환 가능
arr6=[80, 70, 90, 95]
ser2=pd.Series(arr6)
print(ser2.astype(np.float64))
print(ser2.astype(np.float32))
print(ser2.astype(np.float16))
print("\n")

arr7=[0.8, 0.7, 0.9, 0.95]
ser3=pd.Series(arr7)
print(ser3.astype(np.int64))
print(ser3.astype(np.int32))
print(ser3.astype(np.int16))
print("\n")

print(ser1.to_string())
print("\n")
print(str(ser1))
print(ser1)
print("\n")

#DataFrame은 index가 동일한 여러 개의 Seriese로 구성
ser1=df["subject"]
print(ser1)
print(type(ser1))

ser2=df["score"]
print(ser2)
print(type(ser2))

print(ser1.name, ser2.name)
print(ser1.index, ser2.index)
print(ser1.values, ser2.values)
print(type(ser1.values), type(ser2.values))

print(df)
print(df.index)
print(df.columns)
print(df.values)
print(type(df.values))