from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}


@app.post("/turn")
def on_turn(turn_data: dict):
    print("Received turn data:", turn_data)
    response = {
        "reply": "This is a response to your turn.",
        "received_data": turn_data
    }
    return response