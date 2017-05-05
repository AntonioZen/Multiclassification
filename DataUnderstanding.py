import pandas as pd
from colorama import Fore

print(Fore.CYAN)

train = pd.read_csv('C:/DataScience/Kievstar/train.csv', sep = ',')
test = pd.read_csv('C:/DataScience/Kievstar/test.csv', sep = ',')
base1 = pd.read_csv('C:/DataScience/Kievstar/base1.csv', sep = ',')
base2 = pd.read_csv('C:/DataScience/Kievstar/base2.csv', sep = ',')

print(base1)

#data_factors = pd.get_dummies(base1, columns=['T1','T2', 'T3', 'T4', 'T5'])
#print(data_factors)
#exit()
data_factors = base1
for col in data_factors.columns[data_factors.dtypes == "object"]:
    data_factors.loc[data_factors[col].isnull(), col] = 'Missing'
thr = 0.005
for col in data_factors.columns[data_factors.dtypes == "object"]:
    d = dict(data_factors[col].value_counts(dropna=False)/len(data_factors))
    data_factors[col] = data_factors[col].apply(lambda x: 'Rare' if d[x] <= thr else x)
d = dict(data_factors['ID'].value_counts(dropna=False)/len(data_factors))
data_factors = pd.get_dummies(data_factors, columns=['T1','T2', 'T3', 'T4', 'T5'], dummy_na=True)
data_factors.fillna(0)

data_factors.to_csv('C:/DataScience/Kievstar/base1_factors11.csv', sep = ',', index = False)

print(Fore.BLUE)
print(data_factors.head())
