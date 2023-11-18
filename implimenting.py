import numpy as np
from joblib import load

model = load('model\\RandomForest.joblib')

N = float(input("Ratio of Nitrogen content in soil: "))
P = float(input("Ratio of Phosphorous content in soil: "))
O = float(input("Ratio of Potassium content in soil: "))
temperature = float(input("Temperature in degree Celsius: "))
humidity = float(input("Relative humidity in %: "))
ph = float(input("ph value of the soil: "))
rainfall = float(input("Rainfall in mm: "))

data = np.array([[N, P, O, temperature, humidity, ph, rainfall]])
prediction = model.predict(data)
print(prediction)
