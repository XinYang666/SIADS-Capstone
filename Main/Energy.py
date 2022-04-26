import pandas as pd
import datetime as dt
import warnings
import numpy as np
from sklearn.linear_model import LinearRegression
import altair as alt
warnings.filterwarnings('ignore')
pd.set_option('display.max_columns',10)

random_state = 42
df = pd.read_csv("Energy.csv")
df['time'] = pd.to_datetime(df['time'])
mask = (df['time'] < dt.datetime(2022,4,25))
df = df.loc[mask]

def DataResample(df_ori, method):
    df = df_ori.copy()[['time','value']]
    df['time'] = pd.to_datetime(df['time'])
    df.set_index('time', inplace=True)
    df = df.sort_index()
    df = df.resample(method).sum().reset_index()
    return df


def anomaly(data_sensor):
    train_hours = 240  # 10 days
    data_sensor['predict'] = 0
    data_sensor['anomaly'] = 0
    for i in range(len(data_sensor) - train_hours - 1):
        X_train = data_sensor.iloc[i: i + train_hours, 2:-2]
        y_train = data_sensor.iloc[i: i + train_hours, 1]
        lr = LinearRegression().fit(X_train, y_train)
        predict_value = lr.predict(np.array([data_sensor.iloc[i + train_hours + 1, 2:-2]]))[0]
        data_sensor.iloc[i + train_hours + 1, -2] = predict_value
        mean = np.array([data_sensor.iloc[i + train_hours + 1, 2:-2]]).mean()
        # print(data_sensor.iloc[i+train_hours+1]['value'])
        if ((data_sensor.iloc[i + train_hours + 1]['value'] - predict_value) / mean >= degree):  # 3z
            data_sensor.iloc[i + train_hours + 1, -1] = 1

    return data_sensor

sensor_hour_dict = {}
sensor_day_dict = {}

step = 7 # a week
degree = 3 # assume normal distribution
index = 0
for sensor in df[df['sensorId']>400]['sensorId'].unique():
    data = DataResample(df[df['sensorId'] == sensor],'1h')
    for i in range(1,step):
        data[f"t-{i}week"] = data["value"].rolling(window=i * 24 + 1).apply(lambda x: x.iloc[0])


    if ((len(data[data['value']>0])> 200) & (max(data['value'])>4.1) & (max(data['value'])<100)):
        sensor_hour_dict[sensor] = data

        df_anomaly = anomaly(sensor_hour_dict[sensor].dropna())
        if index==0:
            chart = alt.Chart(sensor_hour_dict[sensor]).mark_bar().encode(x='time', y='value').properties(width = 1500,height = 100, title = str(sensor))\
                + alt.Chart(df_anomaly[df_anomaly['anomaly'] == 1]).mark_circle(color='red',size=100).encode(x='time', y='value')
        elif index < 60:
            c = alt.Chart(sensor_hour_dict[sensor]).mark_bar().encode(x='time', y='value').properties(width = 1500,height = 100, title = str(sensor)) \
                + alt.Chart(df_anomaly[df_anomaly['anomaly'] == 1]).mark_circle(color='red',size=100).encode(x='time', y='value')
            chart = alt.vconcat(chart, c)
        index = index + 1

chart.save('meterEnergy_anomaly.html')

sensor_id = 52428
df_sensor = sensor_hour_dict[sensor_id]
df_anomaly = anomaly(df_sensor.dropna())
mask = (df_sensor['time'] < dt.datetime(2022,4,16)) & (df_sensor['time'] > dt.datetime(2022,4,13))
chart_1 = alt.Chart(df_sensor.loc[mask]).mark_bar().encode(x='time', y='value').properties(width = 1000, height = 180, title = str(sensor_id))\
                + alt.Chart(df_anomaly[df_anomaly['anomaly'] == 1].loc[mask]).mark_circle(color='red',size=100).encode(x='time', y='value')

sensor_id = 52604
df_sensor = sensor_hour_dict[sensor_id]
df_anomaly = anomaly(df_sensor.dropna())
mask = (df_sensor['time'] < dt.datetime(2022,4,9)) & (df_sensor['time'] > dt.datetime(2022,4,5))
chart_2 = alt.Chart(df_sensor.loc[mask]).mark_bar().encode(x='time', y='value').properties(width = 1000, height = 180, title = str(sensor_id))\
                + alt.Chart(df_anomaly[df_anomaly['anomaly'] == 1].loc[mask]).mark_circle(color='red',size=100).encode(x='time', y='value')


sensor_id = 52948
df_sensor = sensor_hour_dict[sensor_id]
df_anomaly = anomaly(df_sensor.dropna())
mask = (df_sensor['time'] < dt.datetime(2022,4,10)) & (df_sensor['time'] > dt.datetime(2022,4,2))
chart_3 = alt.Chart(df_sensor.loc[mask]).mark_bar().encode(x='time', y='value').properties(width = 1000, height = 180, title = str(sensor_id))\
                + alt.Chart(df_anomaly[df_anomaly['anomaly'] == 1].loc[mask]).mark_circle(color='red',size=100).encode(x='time', y='value')


chart = alt.vconcat(chart_1,chart_2,chart_3)
chart.save('meterEnergy_anomaly_zoom.html')
