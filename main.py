from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from turn_request import GameState
from turn_request import GameStateResponse

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
    gameState = GameState(**turn_data)
    response = GameStateResponse()
    handle_move(gameState, response)
    target = choose_target(gameState, response)
    shoot(target, gameState, response)
    return response


# choose where to go (escape or go to powerup)
def handle_move(turn_data: GameState, response: GameStateResponse):
    # Implement your move handling logic here
    pass

# choose target (enemy or door)
def choose_target(turn_data: GameState, response: GameStateResponse):
    # Implement your target choosing logic here
    pass
    # return target

def shoot(target, turn_data: GameState, response: GameStateResponse) -> dict:
    # Implement your shooting logic here
    pass