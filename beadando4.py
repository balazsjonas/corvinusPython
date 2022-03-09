import pandas as pd
import pylab as plt


# 1. Rendelések
# a) adat betöltése
df = pd.read_csv('feladat4/orders.tsv', sep='\t')

# b) item_price típus javítása
df['item_price'] = df['item_price'].str.replace('$', '', regex=False).apply(lambda x: float(x))

# c) rendelések összege
df['Sum'] = df['quantity'] *df['item_price']

# d) átlagos rendelés értéke
print('Az átlagos rendelés értéke ${:.2f}'.format(df['Sum'].mean()))

# e-f) az adott ételből hányat adtak el, rendezve
df.groupby('item_name').sum().sort_values(by='quantity')[['quantity']]

# g) dobozos italok
canned_names = ['Canned Soda', 'Canned Soft Drink']
canned = df[(df['item_name'] == canned_names[0]) | ( df['item_name'] == canned_names[1])]

# h) az egyes üdítőkből összesen mennyit rendeltek
soft_drinks = canned.groupby('choice_description').aggregate(sum)[['quantity']]
print(soft_drinks)
soft_drinks.plot(kind='barh')
plt.show()

# 2. rész
import urllib
adsl_filename = 'http://web.uni-corvinus.hu/~fszabina/data/adls_b.txt' # TODO
adsl_filename = 'feladat4/adls_b.txt'
# adsl_columns = 'Start time          	End time            	Activity'
# sensors_filename = 'http://web.uni-corvinus.hu/~fszabina/data/sensors_b.txt'
sensors_filename = 'feladat4/sensors_b.txt'

# a tevékenységre fordított összidő alapján csökkenő sorrendben kiírja az alany tevékenységeit!
adsl = pd.read_csv(adsl_filename, sep=';')
adsl['Starttime'] = pd.to_datetime(adsl['Starttime'])
adsl['Endtime'] = pd.to_datetime(adsl['Endtime'])
adsl['Duration'] = adsl['Endtime'] - adsl['Starttime']
adsl.groupby('Activity').sum().sort_values('Duration', ascending=False)

# adsl2 = pd.read_csv(adsl_filename, sep='\s*\t', engine='python', skiprows=2)
# adsl2[:,0] = pd.to_datetime(adsl2[:,0])
# adsl2[:,1] = pd.to_datetime(adsl2[:,1])
# adsl2['Duration'] = adsl2[1] - adsl2[0]

# b) sensors
sensors = pd.read_csv(sensors_filename, sep=';')
sensors['Starttime'] = pd.to_datetime(sensors['Starttime'])
sensors['Endtime'] = pd.to_datetime(sensors['Endtime'])

limit = pd.to_datetime('2012.11.15 23:59:59')
print(sensors[(sensors['Endtime']<=limit) & (sensors['Place'] == 'Bathroom')])