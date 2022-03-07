import pandas as pd
data1 = {"a": [1, 1, 2], "b": [3.0, 4.0, None]}
df1 = pd.DataFrame(data1)
df1

data = {'color' : ['blue','green','yellow','red','white'],
'object' : ['ball','pen','pencil','paper','mug'],
'price' : [1.2,1.0,0.6,0.9,1.7]}
frame = pd.DataFrame(data)
frame


df = pd.read_csv('data/input/bikes1.csv',sep=';', parse_dates=['Date'], dayfirst=True, index_col='Date', low_memory=False)

#Kiválasztjuk egy oszlopát
berri1=df[['Berri 1']]

complaints = pd.read_csv('data/input/311-service-requests.csv', low_memory=False)
complaints






















