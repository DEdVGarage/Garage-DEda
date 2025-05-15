import pandas as pd
from scipy.stats import kstest
import matplotlib.pyplot as plt
df = pd.read_csv(('D:\Workspace for coding\stats.projects\SP_500_returns.csv'), sep= ';')
print(df)
x = kstest(df['Return_SP_500'], 'norm')
print(x)
a = getattr(x, 'statistic')
b = getattr(x,'pvalue')
print(a)
if b < 0.01 :
    print('распределение не нормальное')
else :
    print("распределение нормальное")   
bp = plt.boxplot(df['Return_SP_500'])    
plt.show()