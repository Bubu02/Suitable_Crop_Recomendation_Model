# Crop Recommendation Model

## Introduction
This README provides an overview of a RandomForest model that recommends suitable crops based on various soil and weather conditions. The model was built using Python and several data science libraries.

## Data Used
The model was trained on a dataset named "crop_recommendation.csv" located in the "Data-processed" directory. This dataset includes features such as Nitrogen, Phosphorus, and Oxygen amounts in the soil, temperature, humidity, pH level, and rainfall.

## Libraries Used
The following Python libraries were used in this project:

- `pandas`
- `numpy`
- `matplotlib.pyplot`
- `seaborn`
- `sklearn.metrics`
- `sklearn.tree`
- `warnings`

## Model Training
The RandomForest model was trained using the above libraries and the "crop_recommendation.csv" dataset. After training, the model was saved using `joblib` for later use.

## Model Usage
The saved model can be loaded and used to make predictions. The model takes as input the Nitrogen, Phosphorus, and Oxygen amounts in the soil, as well as the temperature, humidity, pH level, and rainfall. It then uses these values to make a prediction with your RandomForest model. The prediction will be printed to the console.

## Dependencies
Make sure the following Python libraries are installed in your environment:

- `pandas`
- `numpy`
- `matplotlib`
- `seaborn`
- `scikit-learn`

## Note
Ensure that the path to your model file is correct. If your model file is not in the same directory as your script, you need to provide the full path to the model file. Also, ensure that the 'joblib' and 'numpy' libraries are installed in your Python environment. If they're not, you can install them using pip.

## Implementation
The model has been implemented in a Python file named `implimenting.py`. You can run this file in your Python environment to use the model. If you encounter any issues or need further assistance, feel free to ask. Happy coding! 😊
