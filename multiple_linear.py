import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np
from sklearn.preprocessing import StandardScaler
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn import metrics
from util import Feature_Encoder

data = pd.read_csv('LoanRiskScoreProcessed.csv')
#-1 to specify the last column 
#select the features and store it in x 
#select the dependent variable and store it in y
x = data.iloc[:, [1,2,3,5,6,8,9,10,11,13,14,15,16,17,19,20,21,22]].values
y = data.iloc[:, -1].values

#feature selection using correlation
#accepts boolean and numerical data only
# [0, 2, 4, 5, 6, 9, 11, 12, 13, 14, 15, 16, 17, 19, 20, 21, 22, 23]
corr_df = data.iloc[:, [0, 2, 4, 5, 6, 9, 11, 12, 13, 14, 15, 16, 17, 19, 20, 21, 22, 23]]
corr = corr_df.corr()

#plotting the correlation matrix
plt.figure(figsize=(14,8))
sns.set_theme(style="white")
heatmap = sns.heatmap(corr, annot=True, cmap="Blues", fmt='.1g')
plt.show()

# Categorical encoding
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [0, 2, 5])], remainder='passthrough')
x = pd.DataFrame(ct.fit_transform(x))

# Label Encoding for IsBorrowerHomeowner
x = Feature_Encoder(x, [33])

# Splitting the dataset into the Training set and Test set
# random_state shuffles the training data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1)
x_train = pd.DataFrame(x_train)
x_test = pd.DataFrame(x_test)
y_test = pd.DataFrame(y_test)
y_train = pd.DataFrame(y_train)

# Feature Scaling
x_sc = StandardScaler()
# Compile/Transform on training data, Transform the test data (avoids data leakage)
x_train.iloc[:, 29:] = x_sc.fit_transform(x_train.iloc[:,29:])
x_test.iloc[:,29:] = x_sc.transform(x_test.iloc[:,29:])
y_sc = StandardScaler()
y_train = y_sc.fit_transform(y_train)
y_test = y_sc.transform(y_test)

# Linear Regression Model Initialization
model = LinearRegression()
# Training the model
model.fit(x_train, y_train)

# Predicting the Test set results

y_pred = y_sc.inverse_transform(model.predict(x_test))
y_test = y_sc.inverse_transform(y_test)
# print(np.concatenate((y_pred.reshape(len(y_pred),1), y_test.reshape(len(y_test),1)) , 1))
print(f"Mean Square Error: {metrics.mean_squared_error(np.asarray(y_test), y_pred)}%")
print(f"R2 score : {metrics.r2_score(y_test, y_pred) * 100}%")
print(f"Mean absolute Error: {metrics.mean_absolute_error(y_test, y_pred)}%")