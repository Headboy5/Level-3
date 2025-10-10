import warnings
warnings.filterwarnings('ignore')

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns

advertising = pd.read_csv("C:\\Users\\steph\\OneDrive\\Documents\\University\\Level 3\\Level-3\\Week 3\\Friday - Core Topics\\advertising.csv")
print(advertising.head())
print(advertising.shape)
print(advertising.info())
print(advertising.describe())

sns.pairplot(advertising, x_vars=['TV', 'Newspaper', 'Radio'], y_vars='Sales',size=4, aspect=1, kind='scatter')
# plt.show()
sns.heatmap(advertising.corr(), cmap="YlGnBu", annot = True)
plt.show()

X = advertising['TV']
y = advertising['Sales']
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size = 0.7, test_size = 0.3, random_state = 100)
print(X_train.head())
print(y_train.head())
