import pandas as pd

data={
    "국어": [80, 75, 85, 80],
    "영어": [70, 65, 75, 75],
    "수학": [90, 95, 90, 85],
    "과학": [95, 90, 95, 85]
}

df=pd.DataFrame(data)
print(df)

df=pd.DataFrame(data, index=["June", "July", 'Aug', "Sep"])
print(df)
print("\n")
print(df["국어"].sort_values())
print(df["국어"].sort_index())
print(df["국어"].sort_values(ascending=False))
print(df["국어"].sort_index(ascending=False))

#sort_values()
print(df.sort_values(by="국어"))
print(df.sort_values(by="국어", ascending=False))

#sort_index()
print(df.sort_index())
print(df.sort_index(ascending=False))

#unique():중복이 제거된 데이터를 확인
print(df["국어"].unique())
#nunique():중복이 제거된 데이터 개수를 확인
print(df["국어"].nunique())
#value_counts():값의 개수를 확인
print(df["국어"].value_counts())
print(df["국어"]["June"], df["국어"]["July"])
#slicing
print(df["국어"][1:-1])
print(df[1:-1])

print(df["국어"].min(), df["국어"].max(), df["국어"].median())
print(df["국어"].sum(), df["국어"].mean(), df["국어"].std())
print(df.sum())
print(df.sum(axis=0))
print(df.sum(axis=1))
print(df.min())
print(df.max())
print(df.median())
print(df.mean())
print(df.std())