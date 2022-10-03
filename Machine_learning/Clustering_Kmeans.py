from sklearn.cluster import KMeans
import numpy as np
X = np.array([[1,2],[1,4],[1,0],[10,2],[10,4],[10,0]])
Kmeans = KMeans(n_clusters=2,random_state=0).fit(X)
app = Kmeans.predict([[0,0],[12,3]])
aa =Kmeans.labels_
print(aa)
print(app)

point = Kmeans.cluster_centers_
print(point)