from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
import joblib

# Load the iris dataset
iris = load_iris()
X, y = iris.data, iris.target

#class_names = iris.target_names
#print(class_names)

# Train the model
model = LogisticRegression(max_iter=200)
model.fit(X, y)

# Save the trained model to a file
joblib.dump(model, './Model/model.joblib')
