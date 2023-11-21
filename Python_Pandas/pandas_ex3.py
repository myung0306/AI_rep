import pandas as pd

data={
    "국어": [80, 75, 85, 80],
    "영어": [70, 65, 75, 75],
    "수학": [90, 95, 90, 85],
    "과학": [95, 90, 95, 85]
}

df=pd.DataFrame(data, index=["June", "July", "Aug", "Sep"])

print(df["국어"]+df["영어"])
print(df["국어"]-df["영어"])
print(df["국어"]*df["영어"])
print(df["국어"]/df["영어"])
df["국어/영어 비율"]=df["국어"]/df["영어"]
print(df)

print(df["국어/영어 비율"].apply(lambda x:x*100))

print(df.drop("국어/영어 비율", axis=1))
print(df.drop(["수학", "국어/영어 비율"], axis=1))
print(df[["국어", "영어"]])
print(df.drop("July", axis=0))
print(df.drop(["July", "Aug"], axis=0))
print(df.to_string())
print("\n")

data={
    "국어": [80, 75, 85, 80],
    "영어": [70, 65, 75, 75],
    "수학": [90, 95, 90, 85],
    "과학": [95, 90, 95, 85]
}

df=pd.DataFrame(data, index=["June", "July", "Aug", "Sep"])
print(df)

#loc로 index를 이용해 데이터에 접근
print(df.loc["Sep"])
print(df.loc[["Sep"]])
print(df.loc[["June", "Sep"]])

#iloc로 위치를 이용해 데이터에 접근
print(df.iloc[3])
print(df.iloc[[3]])
print(df.iloc[[0, 3]])