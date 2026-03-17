import numpy as np
from sklearn.cluster import KMeans

x = np.array([[2,50],[4,45],[7,65],[10,70],[12,80]])
centers = np.array([[2,50],[10,70]])

k_means = KMeans(n_clusters=2,init=centers,n_init=1,random_state=42)
k_means.fit(x)

labels = k_means.labels_

for i , labels in enumerate(labels):
    group = "Midlle" if labels == 0 else "Senior"
    print(f"O{i+1} -> {group}")