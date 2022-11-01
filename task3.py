from sklearn.neighbors import KNeighborsClassifier 
import numpy as np 
 
 
 
X = np.array([[25, 40000],[35,60000],[20,20000],[35,120000],[52,18000],[23,95000],[40,62000],[60,100000],[48,220000],[33,150000]]) 
y = ['N','N','N','N','N','N','Y','Y','Y','Y',] 
 
knn = KNeighborsClassifier(n_neighbors=7) 
 
knn.fit(X, y) 
 
print(knn.predict([[42,142000]]))