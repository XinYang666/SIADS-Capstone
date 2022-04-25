
import altair as alt
import pandas as pd
import warnings


warnings.filterwarnings('ignore')
alt.renderers.enable('altair_viewer')

#tempSensorID = [4444,4446,4448,4450,4452,4454,4456,4458,4460,4462,4464,4466,4468,4470,4472,4474,4476,4412,4420,4422,4424,4430,4432,4434,4436,4478,4480,4482,4484,4491,4493,4495,4497,4499,4501,4503,4505,4507,4509,4511,4513]
tempSensorID = [4436,4478,4480,4482,4484,4491,4493,4495,4497,4499,4501,4503,4505,4507,4509,4511,4513]
outdoorTempId = 20003
supplyTempId = 4603
returnTempId = 4602
step = 36 # 3 hours

def DataResample(df):
    df = df.drop_duplicates(subset='createTime', keep='last')
    df['createTime'] = pd.to_datetime(df['createTime'])
    df.set_index('createTime', inplace=True)
    df = df.sort_index()
    df = df.resample('5min').fillna('ffill').reset_index()
    df = df.fillna(method='ffill').dropna()
    return df

def supplyTemp(df):
    df = df[df['sensorId'] == supplyTempId][['createTime', 'value']]

    df = DataResample(df)

    for i in range(1, step):
        df[f"supplyTemp-{i}"] = df["value"].rolling(window=i + 1).apply(lambda x: x.iloc[0])

    df.rename(columns={'value': f"supplyTemp-0"}, inplace=True)
    df.set_index('createTime', inplace=True)
    return df.dropna()

def waterDiff(df):
    df_supply = df[df['sensorId'] == supplyTempId][['createTime', 'value']]
    df_return = df[df['sensorId'] == returnTempId][['createTime', 'value']]

    df_supply = DataResample(df_supply)
    df_return = DataResample(df_return)

    df_diff = pd.merge(df_return, df_supply, how='inner', on='createTime')
    df_diff['waterDiff'] = df_diff['value_x'] - df_diff['value_y']

    df_wd = df_diff[['createTime','waterDiff']]

    for i in range(1, step):
        df_wd[f"waterDiff-{i}"] = df_wd["waterDiff"].rolling(window=i + 1).apply(lambda x: x.iloc[0])

    df_wd.rename(columns={'waterDiff': f"waterDiff-0"}, inplace=True)
    df_wd.set_index('createTime', inplace=True)
    return df_wd.dropna()

def OutdoorTemperature(df):
    df = df[df['sensorId'] == outdoorTempId][['createTime', 'value']]

    df = DataResample(df)

    for i in range(1, step):
        df[f"outdoorTemp-{i}"] = df["value"].rolling(window=i + 1).apply(lambda x: x.iloc[0])

    df.rename(columns={'value': f"outdoorTemp-0"}, inplace=True)
    df.set_index('createTime', inplace=True)
    return df.dropna()

def IndoorTemperature(df):
    i = 0
    for id in tempSensorID:
        df_resample = DataResample(df[df['sensorId'] == id])[['createTime', 'value']]
        if i == 0:
            df_temp = df_resample
            i = 1
        else:
            df_temp = pd.concat([df_temp, df_resample])

    df_temp_avg = df_temp.groupby(by=['createTime']).mean().reset_index()

    for i in range(1, step):
        df_temp_avg[f"indoorTemp-{i}"] = df_temp_avg["value"].rolling(window=i + 1).apply(lambda x: x.iloc[0])

    df_temp_avg.rename(columns = {'value':f"indoorTemp-0"}, inplace = True)
    df_temp_avg.set_index('createTime',inplace = True)
    return df_temp_avg.dropna()


df_07 = pd.read_csv('data07.csv')
df_08 = pd.read_csv('data08.csv')
df_09 = pd.read_csv('data09.csv')

df = pd.concat([df_07,df_08,df_09])

df_all = pd.merge(supplyTemp(df), waterDiff(df),left_index=True,right_index=True)
df_all = pd.merge(df_all,OutdoorTemperature(df),left_index=True,right_index=True)
df_all = pd.merge(df_all,IndoorTemperature(df),left_index=True,right_index=True)

# Normalization
df_norm = (df_all - df_all.min()) / (df_all.max() - df_all.min())

df_all = df_all.reset_index()

df_norm = df_norm.reset_index()

df_all.to_csv("data.csv")

df_norm.to_csv("data_norm.csv")
