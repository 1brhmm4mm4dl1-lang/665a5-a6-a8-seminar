import numpy as np
from sklearn.neighbors import KNeighborsClassifier

x = np.array([[200,1500],[300,1200],[250,1400],[180,1600],[320,1100]])
y = np.array(["s","u","u","s","u"]) # s- sheheretrafi u - sheher

#k = 3
model = KNeighborsClassifier(n_neighbors=3)
model.fit(x,y)

test = np.array([[240,1360]])
pred = model.predict(test)

print(pred[0])





