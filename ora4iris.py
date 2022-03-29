from sklearn import datasets
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# notebooken belül megjeleníti a képet
#%matplotlib inline

#Tibor által ajánlott stílus használata
plt.style.use('ggplot')

iris = datasets.load_iris()
type(iris)

print(iris.keys())
type(iris.data), type(iris.target)
iris.data.shape
iris.target_names
X = iris.data
X
y = iris.target
y


df = pd.DataFrame(X, columns=iris.feature_names)
df
print(df.head())
#pd.scatter_matrix(df, c = y, figsize = [10, 10], s=150, marker = 'D')
pd.plotting.scatter_matrix(df, c = y, figsize = [10, 10], s=150, marker = 'D')
plt.show()


plt.scatter(df['petal length (cm)'], df['petal width (cm)'], c=y)
plt.xlabel('petal length (cm)')
plt.ylabel('petal width (cm)')
plt.grid(True)
plt.show()

#modell importálása
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=8)
knn.fit(iris['data'], iris['target'])
iris['data'].shape
iris['target'].shape

X_new = [[3.0, 3.6, 1.3, 0.25]]
prediction = knn.predict(X_new)
print ('Új minta: {}'.format(X_new))
print('Prediction {}'.format(prediction))

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test =train_test_split(X, y, test_size=0.3, random_state=21, stratify=y)
knn = KNeighborsClassifier(n_neighbors=8)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)
print("Test set predictions:\n {}".format(y_pred))
knn.score(X_test, y_test)