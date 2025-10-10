import warnings
warnings.filterwarnings('ignore')

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
import statsmodels.api as sm
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

advertising = pd.read_csv("C:\\Users\\steph\\OneDrive\\Documents\\University\\Level 3\\Level-3\\Week 3\\Friday - Core Topics\\advertising.csv")
print(advertising.head())
print(advertising.shape)
print(advertising.info())
print(advertising.describe())

# sns.pairplot(advertising, x_vars=['TV', 'Newspaper', 'Radio'], y_vars='Sales',size=4, aspect=1, kind='scatter')
# plt.show()
# sns.heatmap(advertising.corr(), cmap="YlGnBu", annot = True)
# plt.show()

X = advertising['TV']
y = advertising['Sales']
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size = 0.7, test_size = 0.3, random_state = 100)
print(X_train.head())
print(y_train.head())

# Add a constant to get an intercept
X_train_sm = sm.add_constant(X_train)

# Fit the resgression line using 'OLS'
lr = sm.OLS(y_train, X_train_sm).fit()

# Print the parameters, i.e. the intercept and the slope of the regression line fitted
lr.params

# Performing a summary operation lists out all the different parameters of the regression line fitted
print(lr.summary())

plt.scatter(X_train, y_train)
plt.plot(X_train, 6.9897 + 0.0465*X_train, 'r')
plt.show()

# Add a constant to X_test
X_test_sm = sm.add_constant(X_test)

# Predict the y values corresponding to X_test_sm
y_pred = lr.predict(X_test_sm)

y_pred.head()

#Returns the mean squared error; we'll take a square root
np.sqrt(mean_squared_error(y_test, y_pred))

r_squared = r2_score(y_test, y_pred)
r_squared

plt.scatter(X_test, y_test)
plt.plot(X_test, 6.9897 + 0.0465 * X_test, 'r')
plt.show()