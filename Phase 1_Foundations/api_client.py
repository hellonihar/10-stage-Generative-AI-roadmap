# call the hello world API and print the response
import requests

# Define the URL of the API endpoint
url = "http://localhost:8000/"
# Make a GET request to the API
response = requests.get(url)
# Check if the request was successful
if response.status_code == 200:
    # Print the JSON response from the API
    print(response.json())
else:
    print(f"Failed to connect to the API. Status code: {response.status_code}")

# Call the greet endpoint with a name parameter
name = "Alice"
greet_url = f"http://localhost:8000/greet/{name}"
greet_response = requests.get(greet_url)
if greet_response.status_code == 200:
    print(greet_response.json())
else:
    print(
        f"Failed to connect to the greet endpoint. Status code: {greet_response.status_code}"
    )
