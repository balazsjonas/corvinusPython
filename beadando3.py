import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

open_air = pd.read_csv("data/input/openair.csv")
open_air['date'] = pd.to_datetime(open_air['date'])
open_air.set_index('date', inplace=True)
open_air['weekday'] = open_air.index.weekday
open_air.groupby('weekday').aggregate(sum)
open_air.groupby('weekday').aggregate(np.median)
HÉT_MAGYARUL =  ['Hétfő', 'Kedd', 'Szerda', 'Csütörtök', 'Péntek', 'Szombat', 'Vasárnap']

print(df.info)
data = []
for c in df.columns[1:]: # kihagyjuk a dátum oszlopot, mivel ott nincs értelme az átlagnak
    se = df[c]
    data.append({"column": c, "min": se.min(), "max": se.max(), "mean": se.mean()})

stats = pd.DataFrame(data)
print(stats)
print(df["co"].describe())
print(df.describe().info)

df["co"][:168].plot.line()

graf=df["co"][:168]
graf.plot()
plt.show()