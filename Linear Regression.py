#This is a code for linear regression model in machine learning.
# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load

import tensorflow as tf
import keras
import numpy as np

model = keras.Sequential([keras.layers.Dense(units = 1, input_shape = [1])]) # Sequential layers as this is a neural network
model.compile(optimizer = "sgd", loss="mean_squared_error")# stochastic gradient descent as the optimizer
# mean squared error as loss function 

xs = np.array([2.0,3.0,4.0,5.0,6.0,7.0], dtype = float) #storey houses in Los Angles
ys = np.array([20000.0,30000.0,40000.0,50000.0,60000.0,70000.0], dtype = float) # cost of very storey house in Los Angles

model.fit(xs,ys,epochs = 500)
print("The Housing prices in LA for an 8-storey are: ",model.predict([8.0]))
