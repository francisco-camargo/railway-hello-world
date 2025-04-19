from fastapi import FastAPI
import uvicorn, os

app = FastAPI()

@app.get("/")
def root():
    return "Hello, World!"

def start_server():
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=int(os.getenv("PORT", 8000)),  # Railway injects PORT
    )

if __name__ == "__main__":
    start_server()
