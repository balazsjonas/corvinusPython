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