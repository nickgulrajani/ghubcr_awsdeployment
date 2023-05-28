# app.py
import numpy as np
from sklearn.linear_model import LinearRegression

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def get_username(self):
        return self.username

    def get_email(self):
        return self.email

    def train_model(self, X, y):
        model = LinearRegression()
        model.fit(X, y)
        return model

    def predict(self, model, X):
        return model.predict(X)

def main():
    # Create a user
    user = User("JohnDoe", "johndoe@example.com")

    # Prepare training data
    X_train = np.array([[1], [2], [3], [4], [5]])
    y_train = np.array([2, 4, 6, 8, 10])

    # Train a machine learning model
    model = user.train_model(X_train, y_train)

    # Prepare input data for prediction
    X_test = np.array([[6], [7], [8]])

    # Make predictions using the trained model
    predictions = user.predict(model, X_test)

    print("Username:", user.get_username())
    print("Email:", user.get_email())
    print("Predictions:", predictions)

if __name__ == "__main__":
    main()

