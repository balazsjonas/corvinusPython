import pandas as pd
import pylab as plt


print('1. Rendelések\n')
print('a) adatok betöltése')
df = pd.read_csv('orders.tsv', sep='\t')

print('b) item_price típus javítása')
df['item_price'] = df['item_price'].str.replace('$', '', regex=False).apply(lambda x: float(x))

print('c) rendelések összege')
df['Sum'] = df['quantity'] *df['item_price']

print('d) átlagos rendelés értéke')
print('Az átlagos rendelés értéke: ${:.2f}'.format(df['Sum'].mean()))

print('e-f) az adott ételből hányat adtak el, rendezve')
df.groupby('item_name').sum().sort_values(by='quantity')[['quantity']]

print('g) dobozos italok')
canned_names = ['Canned Soda', 'Canned Soft Drink']
canned = df[(df['item_name'] == canned_names[0]) | ( df['item_name'] == canned_names[1])]

print('h) az egyes üdítőkből összesen mennyit rendeltek')
soft_drinks = canned.groupby('choice_description').aggregate(sum)[['quantity']]
print(soft_drinks)
soft_drinks.plot(kind='barh')
plt.title('Rendelések száma üdítőnként')
plt.show()


# 2. rész
print('\n2. rész\n')

# a tevékenységre fordított összidő alapján csökkenő sorrendben kiírja az alany tevékenységeit!
adsl_filename = 'http://web.uni-corvinus.hu/~fszabina/data/adls_b.txt'
adsl = pd.read_csv(adsl_filename, sep='\s*\t', engine='python', skiprows=0)
adsl.drop(0, inplace=True)
adsl.columns = ['Starttime', 'Endtime', 'Activity']
adsl['Starttime'] = pd.to_datetime(adsl['Starttime'])
adsl['Endtime'] = pd.to_datetime(adsl['Endtime'])
adsl['Duration'] = adsl['Endtime'] - adsl['Starttime']
print('Tevékenyégekre fordított idő csökkenő sorrendben')
adsl.groupby('Activity').sum().sort_values('Duration', ascending=False)


# b) sensors

sensors_filename = 'http://web.uni-corvinus.hu/~fszabina/data/sensors_b.txt'
sensors = pd.read_csv(sensors_filename, sep='\t+', engine='python')
sensors.columns = ['Starttime', 'Endtime', 'Location', 'Type', 'Place']
sensors.drop(0, inplace=True)
sensors['Starttime'] = pd.to_datetime(sensors['Starttime'])
sensors['Endtime'] = pd.to_datetime(sensors['Endtime'])

limit = pd.to_datetime('2012.11.15 23:59:59')

print('Fürdőszobában töltött időszakok')
print(sensors[(sensors['Endtime']<=limit) & (sensors['Place'] == 'Bathroom')])
