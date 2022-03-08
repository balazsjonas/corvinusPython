import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

na_values = ["NoData", "InVld", "Maintain", "Samp<", "Span", "ZRef", "Zero"]
names = [
    "Date", "Time", "SO2", "NO", "NO2", "CO", "PM10", "Szels", "Szelir", "Homers",
    "Parat", "Legny", "Naps", "NOx", "PM25", "O3"
]

path = "data/input/legszenny/"
file_names_metro_1 = ['gyor1_2011.csv',
                      'gyor1_2012.csv'
                      ]
file_names_metro_2 = ['gyor2_2011.csv', 'gyor2_2012.csv']
df = pd.DataFrame()
for file in file_names_metro_1:
    skiprows = [i for i, l in enumerate(open(path + file)) if not l[0].isdigit()]
    tmp = pd.read_csv(path + file,
                      skiprows=skiprows,
                      names=names,
                      na_values=na_values,
                      low_memory=False,
                      decimal=','
                      )
    df = pd.concat([df, tmp])

# df.groupby('Time').aggregate(np.mean).plot(kind='box')
# df.groupby('Time')['CO', 'PM10'].aggregate(np.median)
df.groupby('Time').aggregate(np.median)[['CO', 'PM10']].plot()  # ?????????
plt.show()
