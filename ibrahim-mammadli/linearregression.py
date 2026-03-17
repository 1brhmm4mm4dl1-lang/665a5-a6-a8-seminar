import numpy as np
from sklearn.linear_model import LinearRegression

X = np.array([100,200,300,400,500]).reshape(-1, 1)
y = np.array([500,1000,1500,2000,2500])

model = LinearRegression()
model.fit(X,y)

x_new = np.array([[350]])
pred = model.predict(x_new)

print(pred[0])

