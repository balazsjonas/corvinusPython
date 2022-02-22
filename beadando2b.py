import numpy as np
import urllib.request as ur

# Közvetlenül az internetről is letölthetjük az adatokat, az alábbi módon:
url1= ur.urlopen("http://web.uni-corvinus.hu/~fszabina/data/wine.data")
data1 = np.loadtxt(url1, delimiter=",")


# wine.name állomány alapján az oszlopok jelentése
columns = [
    "Alcohol", "Malic acid", "Ash", "Alcalinity of ash", "Magnesium",
    "Total phenols", "Flavanoids", "Nonflavanoid phenols", "Proanthocyanins", "Color intensity",
    "Hue", "OD280/OD315 of diluted wines", "Proline",
]

borok = data1[:,1:]
#töltsük be az ismeretlen bor jellemzői
url2= ur.urlopen("http://web.uni-corvinus.hu/~fszabina/data/wine.unknown")
data2 = str(url2.read())

t=data2.split(",")
ismeretlenbor=[]
for e in t:
    b=e.split(": ")
    ismeretlenbor.append(float(b[1].replace("'", "")))

ibor=np.array(ismeretlenbor)
####################
# Innentől saját szerzemény

def print_std(data):
    width = len(max(columns, key=len))
    for i in range(data.shape[1]):
        print('{col:>{width}}: {std:<5.2f}'.format(width = width, col = columns[i], std=data[:, i].std()))

print("Eredeti szórások:")
print_std(borok)


normalized = np.zeros_like(borok)
stds = np.zeros((borok.shape[1]))
print("Normalizált szórások:")
for i in range(borok.shape[1]):
    stds[i] = borok[:, i].std()
    normalized[:,i] = borok[:,i] / stds[i]
print_std(normalized)


np.argmin()