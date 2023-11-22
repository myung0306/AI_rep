import pandas as pd

data={
    "subjec":["국어", "영어", None, "과학"],
    "score":[80, None, 90, 95]
}

df_tmp=pd.DataFrame(data)
print(df_tmp.fillna(9999))

#errors='coerce'옵션으로 오류난 데이터는 NaT로 저장
df=pd.read_csv("C:\\AI_repo\\Python_Pandas\\data.csv")
date1=pd.to_datetime(df["Date"], format='\'%Y/%m/%d\'', errors='coerce')
print(date1)

#오류가 발생한 'Date'를 다른 형식으로 Parsing
df=pd.read_csv("C:\\AI_repo\\Python_Pandas\\data.csv")
date2=pd.to_datetime(df["Date"], format='%Y/%m/%d', errors='coerce')
print(date2)

date3=date1.fillna(date2)
print(date3)

df["Date"]=date3
print(df)

print(df.info())

#set_index()
df.set_index("Date", inplace=True)
print(df)
print(df.reset_index())
#sort_index()명령을 이용해서 indxe 기준으로 정렬
print(df.sort_index())
#sort_index()명령에 ascending=False옵션을 추가해서 역순으로 정렬
print(df.sort_index(ascending=False))
print(df.loc["2020-12-01"])
print(df.loc["2020-12-01":"2020-12-10"])
print(pd.date_range("2020-12-01", "2020-12-10"))
print(pd.date_range("2020-12-01", periods=5))
print(pd.date_range("2020-12-01", freq="W-SUN", periods=3))
print(df.loc[pd.date_range("2020-12-01", periods=5)])
print(df.loc[pd.date_range("2020-12-01", freq="W-SUN", periods=3)])

df["Year"]=df.index.year
df["Month"]=df.index.month
df["Day"]=df.index.day
df["Quater"]=df.index.quarter
df["DoW"]=df.index.day_of_week
print("-"*100)
print(df)

df3=pd.read_csv("C:\\AI_repo\\Python_Pandas\\data.csv")
print(pd.date_range("2020-12-15","2020-12-20"))

data = {
    '국어': [80, 75, 85, 80],
    '영어': [70, 65, 75, 75],
    '수학': [90, 95, 90, 85],
    '과학': [95, 90, 95, 220]
}

df1=pd.DataFrame(data, index=["June", "July", "Aug", "Sep"])
print(df1)

data = {
    '미술': [90, 85, 80, 95, 90],
    '체육': [80, 85, 75, 70, 80],
    '음악': [80, 75, 70, 75, 80]
}

df2=pd.DataFrame(data, index=["June", "July", "Aug", "Sep", "Nov"])
print(df2)

df_all=pd.concat([df1, df2])
print(df_all)

df_all=pd.concat([df1, df2], axis=1)
print(df_all)

print(0<=df_all["과학"])
print(df_all["과학"]<=100)
print((0<=df_all["과학"])&(df_all["과학"]<=100))
print((0<=df_all["과학"])|(df_all["과학"]<=100))
print(df_all[df_all["과학"]>=100])
print(df_all.drop(df_all[df_all["과학"]>=100].index))

#duplicated()
data = {
    '국어': [80, 75, 85, 80, 75],
    '영어': [70, 65, 75, 75, 65],
    '수학': [90, 95, 90, 85, 95],
    '과학': [95, 90, 95, 220, 90]
}

df1 = pd.DataFrame(data, index=['June', 'July', 'Aug', 'Sep', 'Nov'])
print(df1.duplicated())
print(df1.drop_duplicates())
print(df1[df1.duplicated()])
print(df1.drop(df1[df1.duplicated()].index))
print(df1.loc["Sep", "과학"])
df1.loc["Sep", "과학"]=95
print(df1)

#Mission
df.duplicated()
df.drop_duplicates(inplace=True)


print(df[df["Duration"]>100])
df.loc[df[df["Duration"]>100].index, "Duration"]=90
print(df)