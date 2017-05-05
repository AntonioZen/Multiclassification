import pandas as pd
from colorama import Fore

data_base2 = pd.read_csv('C:/Users/antonio/Desktop/Kievs/base2.csv', sep = ',')
data_train = pd.read_csv('C:/Users/antonio/Desktop/Kievs/train.csv', sep = ',')

print(Fore.LIGHTYELLOW_EX)
print(data_base2.head())

MONTH = [1,2,3,4,5,6]
df = data_train
for M in MONTH:
    data = data_base2.loc[data_base2['MONTH_AGO'] == M]
    data = data.drop(['MONTH_AGO'], axis=1)
    df = df.merge(data,on='ID',how='left', suffixes=('', '_MONTH_'+str(M)))
    print(df)
    print('_MONTH_'+str(M))

print(Fore.CYAN)
print(df.head())

df.to_csv('C:/Users/antonio/Desktop/Kievs/train_base2.csv', sep = ',')

datasetX_mean = df.mean()
datasetX_std = df.std()

X_variables = df.columns.tolist()
print(X_variables)
print(type(X_variables))
X_variables[0:2] = []

print(X_variables)
for col in X_variables:
    print(col)
    #cok = unicode(col, "utf-8")
    df[col] = df[col].clip(
        datasetX_mean[col]-2.6*datasetX_std[col],
        datasetX_mean[col]+2.6*datasetX_std[col])

print(df)

datasetX_mean2 = df.mean()

df.fillna(datasetX_mean2, inplace=True)
print(Fore.LIGHTYELLOW_EX)
print(df)
