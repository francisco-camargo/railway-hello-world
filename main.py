from fastapi import FastAPI
import uvicorn, os

app = FastAPI()

@app.get("/")
def root():
    return "Hello, World!"

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=int(os.getenv("PORT", 8000)),  # Railway injects PORT
    )
