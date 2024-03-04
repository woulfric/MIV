import numpy as np
from sklearn.linear_model import LinearRegression
from matplotlib import pyplot as plt 

x = np.array([5, 15, 25, 35, 45, 55])
print(x)
#Pass the value -1 , NumPy will calculate this number for you.
x = np.array([5, 15, 25, 35, 45, 55]).reshape((-1, 1))
print(x)
y = np.array([5, 20, 14, 32, 22, 38])
print(y)

model = LinearRegression()
model.fit(x, y)
r_sq = model.score(x, y) # return the error
print('coefficient of determination:', r_sq)
# The attributes of model are .intercept_, which represents the coefficient, 𝑏₀ 
# and .coef_, which represents 𝑏₁:
print('intercept:', model.intercept_) # b, y=ax+b
print('slope:', model.coef_) #a
xp = np.array([40, 30]).reshape((-1, 1))
y_pred = model.predict(xp)
print('predicted response:', y_pred, sep='\n')
# x=15, y=0.54*15+5.63=13,73

plt.scatter(x, y,color='g') 
plt.plot(xp, y_pred,color='k') 

plt.show()