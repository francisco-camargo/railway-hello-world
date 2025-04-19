'''
FastAPI Hello World application for Railway deployment.

This module provides a simple FastAPI application that serves a "Hello, World!"
message. It can be run locally using uvicorn or deployed to Railway.

To start the server locally, run:
    uvicorn main:app --reload
'''

from fastapi import FastAPI
import uvicorn, os

app = FastAPI()

@app.get("/")
def root() -> str:
    '''
    Return a greeting message.
    '''

    return "Hello, World!"

def start_server() -> None:
    '''
    Start the uvicorn server with the FastAPI application.

    The server will run on host 0.0.0.0 and use the PORT environment
    variable (defaulting to 8000) as specified by Railway's requirements.
    '''
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=int(os.getenv("PORT", 8000)),  # Railway injects PORT
    )

if __name__ == "__main__":
    start_server()
