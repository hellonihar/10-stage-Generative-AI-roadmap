# create a simple linear regression model to predict house prices based on the size of the house
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


def house_price_prediction():
    # Generate synthetic data for house sizes and prices
    np.random.seed(42)
    house_sizes = np.random.rand(100, 1) * 2000  # House sizes in square feet
    house_prices = house_sizes * 150 + (
        np.random.rand(100, 1) * 50000
    )  # Prices with some noise

    # Split the data into training and testing sets
    split_index = int(0.8 * len(house_sizes))
    X_train, X_test = house_sizes[:split_index], house_sizes[split_index:]
    y_train, y_test = house_prices[:split_index], house_prices[split_index:]

    # Create a linear regression model
    model = LinearRegression()

    # Fit the model to the training data
    model.fit(X_train, y_train)

    # Make predictions on the test set
    y_pred = model.predict(X_test)

    # Evaluate the model's performance using Mean Absolute Error
    mae = np.mean(np.abs(y_test - y_pred))
    print(f"Mean Absolute Error: {mae:.2f}")

    # Plot the results
    plt.scatter(X_test, y_test, color="blue", label="Actual Prices")
    plt.scatter(X_test, y_pred, color="red", label="Predicted Prices")
    plt.xlabel("House Size (sq ft)")
    plt.ylabel("House Price ($)")
    plt.title("House Price Prediction")
    plt.legend()
    plt.show()


# Run the house price prediction demo
if __name__ == "__main__":
    house_price_prediction()
