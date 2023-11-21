import pandas as pd

data={
    "subjec":["국어", "영어", None, "과학"],
    "score":[80, None, 90, 95]
}

df_tmp=pd.DataFrame(data)
print(df_tmp.fillna(9999))