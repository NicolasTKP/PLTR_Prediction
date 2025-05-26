from joblib import load
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import joblib
from keras.models import Sequential, load_model

scaler = joblib.load("scaler.pkl")
model = load_model("stock_price_model.h5")
df = pd.read_csv('PLTR.csv')
df = df.iloc[::-1].reset_index(drop=True)

#comment everything below this line to test the accuracy of the model
new_row = pd.DataFrame({'Date': [11022025], 'Open': [116.50], 'High': [116.50], 'Low': [116.50], 'Close': [116.50], 'Adj_Close': [116.50], 'Volume': [116.50]})
df = pd.concat([df, new_row], ignore_index=True)
df = df.tail(60)


def test_accuracy():
    dataset_test = pd.read_csv('PLTR_latest.csv') #retrieve the latest data to test the model
    dataset_test = dataset_test.iloc[::-1].reset_index(drop=True)
    actual_stock_price = dataset_test.iloc[:, 1:2].values
    open_price = df.iloc[:, 1:2].values
    inputs = open_price[len(df) - len(dataset_test) - 60:] #Get the last 60 days of the data to predict the next 30 days

    inputs = inputs.reshape(-1, 1) #Reshape the data to be 2D
    inputs = scaler.transform(inputs) #Normalize the data
    # show_inputs = scaler.inverse_transform(inputs)
    # print(f'input: {show_inputs}')
    print(f'actual: {actual_stock_price[-1]}')

    X_test = []
    for i in range(60, 60 + len(dataset_test)): #Make X be the previous 60 days
        X_test.append(inputs[i-59:i+1, 0])
    X_test = np.array(X_test)
    show_inputs = scaler.inverse_transform(X_test)
    print(f'input: {show_inputs[-1]}')

    X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1)) #Reshape the data to be 3D

    predicted_stock_price =  model.predict(X_test) #Predict the next 30 days
    predicted_stock_price = scaler.inverse_transform(predicted_stock_price) #Denormalize the data

    print(predicted_stock_price)

    plt.plot(actual_stock_price, color = 'red', label = 'Actual Stock Price')
    plt.plot(predicted_stock_price, color = 'blue', label = 'Predicted Stock Price')
    plt.title('Stock Price Prediction')
    plt.xlabel('Time')
    plt.ylabel('Stock Price')
    plt.legend()
    plt.show()


def prediction():
    open_price = df.iloc[:, 1:2].values
    inputs = scaler.transform(open_price)

    X = np.reshape(inputs, (inputs.shape[1], inputs.shape[0], 1))
    print(X)
    print(X.shape)
    predicted_stock_price =  model.predict(X) #Predict the next 30 days
    predicted_stock_price = scaler.inverse_transform(predicted_stock_price) #Denormalize the data
    print(predicted_stock_price)

prediction()