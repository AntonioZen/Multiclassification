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
    df = df.merge(data,on='ID',how='left', suffixes=('', '_MONTH_'+str(M)))
    print(df)
    print('_MONTH_'+str(M))

print(Fore.CYAN)
print(df.head())

df.to_csv('C:/Users/antonio/Desktop/Kievs/train_base2.csv', sep = ',')
