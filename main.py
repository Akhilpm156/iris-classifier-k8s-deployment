from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()

# Load the trained model
model = joblib.load("./Model/model.joblib")
class_names = ['setosa','versicolor','virginica']

class InputData(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

@app.post("/predict")
def predict(data: InputData):
    # Prepare the input data
    input_array = np.array([[data.sepal_length, data.sepal_width, data.petal_length, data.petal_width]])
    
    # Predict the class using the model
    prediction = model.predict(input_array)
    return {"prediction": class_names[int(prediction[0])]}
