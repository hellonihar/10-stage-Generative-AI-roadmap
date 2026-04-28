# hello_world_api.py
from fastapi import FastAPI

# Create the FastAPI app instance
app = FastAPI()


# Define a simple GET endpoint
@app.get("/")
def read_root():
    return {"message": "Hello, World!"}


@app.get("/greet/{name}")
def greet(name: str):
    return {"message": f"Hello, {name}!"}
