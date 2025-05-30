"""
This module contains the FastAPI application with endpoints for 
status, greeting, summing numbers, and writing a file.
"""

from fastapi import FastAPI
from pydantic import BaseModel
from app import say_hi

app = FastAPI(
    title="Simple FastAPI Server",
    description="A FastAPI server with status and greeting endpoints.",
    version="1.0.0"
)

@app.get("/status")
def get_status() -> dict:
    """Returns the server status."""
    return {"status": "OK"}

@app.get("/version")
def get_version() -> dict:
    """Returns the server version."""
    return {"status": "1.1"}

@app.get("/sayhi/{name}")
def say_hi_name(name: str) -> dict:
    """Greets the user with their provided name."""
    return {"message": f"Hi, {name}!"}

@app.get("/writefile")
def write_file() -> dict:
    """Triggers file writing logic from app.py and returns file path."""
    path = say_hi("File written from API!")
    return {"file_path": path}

class SumRequest(BaseModel):
    """Request model for summing two numbers."""
    a: int
    b: int

@app.post("/sum")
def sum_numbers(data: SumRequest) -> dict:
    """Returns the sum of two numbers using a POST request."""
    return {"sum": data.a + data.b}
