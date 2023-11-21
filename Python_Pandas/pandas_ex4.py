import pandas as pd

df=pd.read_csv("C:\\AI_repo\\Python_Pandas\\data.csv")
#print(df)
#print(df.to_string())

df1=pd.read_csv("C:\\AI_repo\\Python_Pandas\\data.csv", delimiter="\t")
#print(df1)

#head
print(df.head())
print(df.head(10))

#tail
print(df.tail())
print(df.tail(10))

#info
print(df.info())

#isna():NaN여부 확인
df2=df.isna()
print(df2)

print(df2.sum())
print(df2.sum(axis=1))

#dropna:NaN이 존재하는 데이터 삭제
df2=df.dropna()
print(df2)
df2=df.dropna(axis=1)
print(df2)
df2=df.dropna(ignore_index=True)
print(df2)
df.dropna()
print(df)
df.dropna(inplace=True)
print(df)

#len()
df=pd.read_csv("C:\\AI_repo\\Python_Pandas\\data.csv")
print(df)
df2=df.dropna()
print(len(df), len(df2))

df.dropna(subset=["Date"], inplace=True, ignore_index=True)
print(df)
print(df.info())
print(df.describe())

#산술 평균 : 주어진 수의 합을을 수의 개수로 나눈 값
#표준 편차 : 통계집단의 분산의 정도 또는 자료의 산포도를 나타내는 수치, 분산의 음이 아닌 제곱근 즉, 분산을 제곱근한 것으로 정의
#사분위수 : 데이터를 4등분 한 것

df1=df.copy()
mean=df1["Calories"].mean()
df1["Calories"].fillna(mean, inplace=True)
print(df1)

median=df1["Calories"].median()
df1["Calories"].fillna(median, inplace=True)
print(df1)

mode=df1["Calories"].mode()[0]
df1["Calories"].fillna(mode, inplace=True)
print(df1)

s=pd.Series([2, 4, 2, 2, 4, None])
print(s.mode())
s=pd.Series([2, 4, 8, 2, 4, None])
print(s.mode())
print(df["Calories"].mode())

#ffill():이전 값을 NaN에 적용
df1=df.copy()
print(df1["Calories"].ffill(inplace=True))
print(df1)

#bfill():이후 값을 NaN에 적용
df1=df.copy()
print(df["Calories"].bfill(inplace=True))
print(df1)

mean=df["Calories"].mean()
print(df["Calories"].fillna(mean, inplace=True))
print(df)

df=pd.read_csv("C:\\AI_repo\\Python_Pandas\\data.csv")
print(df)
df3=df.copy()
df3.dropna(subset=["Calories"], inplace=True, ignore_index=True)
print("\n")
print(df3)
print(df3.info())

median=df3["Calories"].median()
df3["Calories"].fillna(median, inplace=True)
print(df3)

mean=df3["Calories"].mean()
df3["Calories"].fillna(mean, inplace=True)
print(df3)