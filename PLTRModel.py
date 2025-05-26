from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import accuracy_score, mean_squared_error
import pandas as pd
from joblib import dump
import os 
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
import numpy as np
from sklearn.model_selection import train_test_split
from keras.models import Sequential, load_model
from keras.layers import Dense, LSTM, Dropout
import joblib

def data_cleaning(df):
    training_set = df.iloc[:, 1:2].values # open price

    scaler = MinMaxScaler(feature_range=(0, 1)) #Normalize the data to make it between 0 and 1
    scalesd_training_set = scaler.fit_transform(training_set)
    joblib.dump(scaler, "scaler.pkl") 
    X_train = []
    y_train = []
    for i in range(60, len(scalesd_training_set)): #Make X be the previous 60 days and y be the next day
        X_train.append(scalesd_training_set[i-60:i, 0])
        y_train.append(scalesd_training_set[i, 0])
    X_train, y_train = np.array(X_train), np.array(y_train) 

    X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1)) #Reshape the data to be 3D

    return X_train, y_train

def model_training(X_train, y_train, df):
    regressor = Sequential() #A model that can fit layer by layer (deep learning => input -> hidden -> output)

    regressor.add(LSTM(units=50, return_sequences=True, input_shape=(X_train.shape[1], 1))) #first hidden layer
    regressor.add(Dropout(0.2)) #Dropout some neuron to prevent overfitting

    regressor.add(LSTM(units=50, return_sequences=True)) #second hidden layer
    regressor.add(Dropout(0.2))

    regressor.add(LSTM(units=50, return_sequences=True)) #third hidden layer
    regressor.add(Dropout(0.2))

    regressor.add(LSTM(units=50)) #fourth hidden layer
    regressor.add(Dropout(0.2))

    regressor.add(Dense(units=1)) #output layer

    regressor.compile(optimizer='adam', loss='mean_squared_error') #Compile the model
    regressor.fit(X_train, y_train, epochs=100, batch_size=32) #Fit the model

    regressor.save("stock_price_model.h5") 
    scaler = joblib.load("scaler.pkl")

    dataset_test = pd.read_csv('PLTR_latest.csv') #retrieve the latest data to test the model
    dataset_test = dataset_test.iloc[::-1].reset_index(drop=True)
    actual_stock_price = dataset_test.iloc[:, 1:2].values
    open_price = df.iloc[:, 1:2].values
    inputs = open_price[len(df) - len(dataset_test) - 60:].values #Get the last 60 days of the data to predict the next 30 days
    
    inputs = inputs.reshape(-1, 1) #Reshape the data to be 2D
    inputs = scaler.transform(inputs) #Normalize the data
    show_inputs = scaler.inverse_transform(inputs)
    print(f'input: {show_inputs[-1]}')
    print(f'actual: {actual_stock_price[-1]}')

    X_test = []
    for i in range(60, 60 + len(dataset_test)): #Make X be the previous 60 days
        X_test.append(inputs[i-60:i, 0])
    X_test = np.array(X_test)
    X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1)) #Reshape the data to be 3D
    
    predicted_stock_price = regressor.predict(X_test) #Predict the next 30 days
    predicted_stock_price = scaler.inverse_transform(predicted_stock_price) #Denormalize the data

    print(predicted_stock_price)

    plt.plot(actual_stock_price, color = 'red', label = 'Actual Stock Price')
    plt.plot(predicted_stock_price, color = 'blue', label = 'Predicted Stock Price')
    plt.title('Stock Price Prediction')
    plt.xlabel('Time')
    plt.ylabel('Stock Price')
    plt.legend()
    plt.show()

if __name__ == '__main__':
    df = pd.read_csv('PLTR.csv')
    df = df.iloc[::-1].reset_index(drop=True)
    X_train, y_train = data_cleaning(df)
    model_training(X_train, y_train, df)