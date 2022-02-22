import numpy as np
import urllib.request as ur

# Közvetlenül az internetről is letölthetjük az adatokat, az alábbi módon:
url1= ur.urlopen("http://web.uni-corvinus.hu/~fszabina/data/wine.data")
data1 = np.loadtxt(url1, delimiter=",")


#wine.name állomány alapján az oszlopok jelentése
columns = [
    "Alcohol", "Malic acid", "Ash", "Alcalinity of ash", "Magnesium",
    "Total phenols", "Flavanoids", "Nonflavanoid phenols", "Proanthocyanins", "Color intensity",
    "Hue", "OD280/OD315 of diluted wines", "Proline",
]

#data1 mátrix sorainak első eleme a borászat azonosítója
azonosito=data1[:, 0]

#a sor további jellemzői az adott bor jellemzői
borok=data1[:, 1:]

#Nézzük meg a borok alapvető statisztikai jellemzőit, azaz min, max, mean, szórás

#lekérdezzük a méretet (azaz hány bor adatunk van és hány különböző jellemzőn)
borok.shape

#borok tömbön a különböző jellemzők esetén kiszámoljuk statisztikai jellemzőket
for j in range(borok.shape[1]):
    Xj = borok[:, j]
    print(j, columns[j], Xj.min(), Xj.max(), Xj.mean(), Xj.std())
for j in range(borok.shape[1]):
    Xj = borok[:, j]
    print(f"{j}. paraméter, {columns[j]} átlaga: {Xj.mean()}")

#töltsük be az ismeretlen bor jellemzői
url2= ur.urlopen("http://web.uni-corvinus.hu/~fszabina/data/wine.unknown")
data2 = str(url2.read())

# np.loadtxt(url2, delimiter=": ") nem működik, mert a fájl szöveges adatokat is tartalmaz
t=data2.split(",")
ismeretlenbor=[]
for e in t:
    b=e.split(": ")
    ismeretlenbor.append(float(b[1].replace("'", "")))

ibor=np.array(ismeretlenbor)


#Ábrázoljuk a borokat - később vesszük a matplotlib modult.
import matplotlib.pyplot as plt

c1, c2 = 6, 11
plt.scatter(borok[azonosito == 1, c1], borok[azonosito == 1, c2], c="red")
plt.scatter(borok[azonosito == 2, c1], borok[azonosito == 2, c2], c="green")
plt.scatter(borok[azonosito == 3, c1], borok[azonosito == 3, c2], c="blue")
plt.scatter(ibor[c1], ibor[c2], s=100, c="yellow")
plt.xlabel(columns[c1])
plt.ylabel(columns[c2])
plt.grid(True)