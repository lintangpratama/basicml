# Import the library
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Read the csv file
dataset = pd.read_csv('D:\Sales_Data.csv PATH')

# Make a X and Y variable that declares the cost of promo and revenue
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values

dataku = pd.DataFrame(dataset)

# Splitting the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# Fitting Simple Linear Regression
regressor = LinearRegression()
model = regressor.fit(X_train, y_train)

# Data Visualization
plt.scatter(dataku.BiayaPromo, dataku.NilaiPenjualan)
plt.title('Dataset')
plt.xlabel('Biaya Promosi')
plt.ylabel('Penjualan')
plt.show

# Data visualization for training set
plt.figure(figsize = (7,5))
plt.scatter(X_train, y_train, color='blue')
plt.plot(X_train, regressor.predict(X_train), color='green')
plt.title('Biaya Promosi terhadap Penjualan (Training Set)')
plt.xlabel('Biaya Promosi')
plt.ylabel('Penjualan')
plt.show()

#Data visualization for test set
plt.figure(figsize = (7,5))
plt.scatter(X_test, y_test, color='blue')
plt.plot(X_test, regressor.predict(X_test), color='green')
plt.title('Biaya Promosi terhadap Penjualan (Predict)')
plt.xlabel('Biaya Promosi')
plt.ylabel('Penjualan')
plt.show()