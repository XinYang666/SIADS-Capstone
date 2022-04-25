
import pandas as pd
import datetime as dt
import warnings



warnings.filterwarnings('ignore')
pd.set_option('display.max_columns',10)

random_state = 42

def labelData(df, start_date, end_date):
    mask = (df['createTime'] > start_date) & (df['createTime'] <= end_date)
    df.loc[mask,'efficient'] = 1
    return df

data = pd.read_csv('data.csv')
data['createTime'] = pd.to_datetime(data['createTime'])
data['efficient'] = 0
#data_norm = pd.read_csv('data_norm.csv')

data = labelData(data, dt.datetime(2021,7,6,2), dt.datetime(2021,7,6,8))
data = labelData(data, dt.datetime(2021,7,8,22), dt.datetime(2021,7,9,3))


data = labelData(data, dt.datetime(2021,8,2,0), dt.datetime(2021,8,2,7))
data = labelData(data, dt.datetime(2021,8,17,0), dt.datetime(2021,8,17,8))
data = labelData(data, dt.datetime(2021,8,18,0), dt.datetime(2021,8,18,8))
data = labelData(data, dt.datetime(2021,8,19,16), dt.datetime(2021,8,20,0))
data = labelData(data, dt.datetime(2021,8,21,0), dt.datetime(2021,8,20,6))
data = labelData(data, dt.datetime(2021,8,22,0), dt.datetime(2021,8,22,6))
data = labelData(data, dt.datetime(2021,8,24,2), dt.datetime(2021,8,24,6))
data = labelData(data, dt.datetime(2021,8,25,2), dt.datetime(2021,8,25,8))
data = labelData(data, dt.datetime(2021,8,26,3), dt.datetime(2021,8,26,9))
data = labelData(data, dt.datetime(2021,8,27,8), dt.datetime(2021,8,27,6))
data = labelData(data, dt.datetime(2021,8,27,22), dt.datetime(2021,8,28,7))
data = labelData(data, dt.datetime(2021,8,28,22), dt.datetime(2021,8,29,7))
data = labelData(data, dt.datetime(2021,8,30,0), dt.datetime(2021,8,30,7))

data = labelData(data, dt.datetime(2021,8,31,22), dt.datetime(2021,9,1,7))
data = labelData(data, dt.datetime(2021,9,1,22), dt.datetime(2021,9,2,7))
data = labelData(data, dt.datetime(2021,9,6,20), dt.datetime(2021,9,7,8))
data = labelData(data, dt.datetime(2021,9,7,22), dt.datetime(2021,9,8,6))
data = labelData(data, dt.datetime(2021,9,9,4), dt.datetime(2021,9,9,8))

data = labelData(data, dt.datetime(2021,9,9,4), dt.datetime(2021,9,9,8))
data = labelData(data, dt.datetime(2021,9,9,4), dt.datetime(2021,9,9,8))
data = labelData(data, dt.datetime(2021,9,9,4), dt.datetime(2021,9,9,8))
data = labelData(data, dt.datetime(2021,9,9,4), dt.datetime(2021,9,9,8))
data = labelData(data, dt.datetime(2021,9,9,4), dt.datetime(2021,9,9,8))
data = labelData(data, dt.datetime(2021,9,9,4), dt.datetime(2021,9,9,8))
data = labelData(data, dt.datetime(2021,9,9,4), dt.datetime(2021,9,9,8))
data = labelData(data, dt.datetime(2021,9,9,4), dt.datetime(2021,9,9,8))
data = labelData(data, dt.datetime(2021,9,10,0), dt.datetime(2021,9,10,8))
data = labelData(data, dt.datetime(2021,9,14,22), dt.datetime(2021,9,15,8))
data = labelData(data, dt.datetime(2021,9,15,22), dt.datetime(2021,9,16,7))
data = labelData(data, dt.datetime(2021,9,17,3), dt.datetime(2021,9,17,7))
data = labelData(data, dt.datetime(2021,9,17,22), dt.datetime(2021,9,18,8))
data = labelData(data, dt.datetime(2021,9,19,22), dt.datetime(2021,9,21,9))
data = labelData(data, dt.datetime(2021,9,21,22), dt.datetime(2021,9,22,9))

mask = ((data['createTime'] >= dt.datetime(2021,7,1,0)) & (data['createTime'] < dt.datetime(2021,7,10,0))) |\
    ((data['createTime'] >= dt.datetime(2021,8,1,0)) & (data['createTime'] < dt.datetime(2021,8,10,0))) |\
    ((data['createTime'] >= dt.datetime(2021,9,1,0)) & (data['createTime'] < dt.datetime(2021,9,10,0)))
X_train = data.loc[mask].iloc[:,2:-1]
y_train = data.loc[mask].iloc[:,-1]

X_test = data.loc[~mask].iloc[:,2:-1]
y_test = data.loc[~mask].iloc[:,-1]

X_train.index.name = 'index'
X_test.index.name = 'index'
y_train.index.name = 'index'
y_test.index.name = 'index'

X_train.to_csv('X_train.csv')
y_train.to_csv('y_train.csv')
X_test.to_csv('X_test.csv')
y_test.to_csv('y_test.csv')
