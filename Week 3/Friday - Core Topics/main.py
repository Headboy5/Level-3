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