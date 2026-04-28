import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


def supervised_learning_demo():
    # Load the Iris dataset
    iris = load_iris()
    X = iris.data  # Features
    y = iris.target  # Target labels

    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Create a K-Nearest Neighbors classifier
    knn = KNeighborsClassifier(n_neighbors=3)

    # Fit the model to the training data
    knn.fit(X_train, y_train)

    # Make predictions on the test set
    y_pred = knn.predict(X_test)

    # Evaluate the accuracy of the model
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Accuracy: {accuracy:.2f}")
    # Let's predict the species for the first three unseen samples.

    sample_to_predict = X_test[:3]
    predicted_classes = knn.predict(sample_to_predict)
    print("\nInference Example] Predicting for the first 3 test samples:\n")
    # print a new line for each sample and the predicted class name

    for i, pred in enumerate(predicted_classes):
        print(f"Sample {i + 1}: Predicted class = {iris.target_names[pred]}")


if __name__ == "__main__":
    supervised_learning_demo()
