from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from turn_request import *
from turn_response import *

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
    gameState = GameState(**turn_data)
    response = PlayerCommand(move=Move(direction=0.0, speed=0.0))
    handle_move(gameState, response)
    target = choose_target(gameState, response)
    shoot(target, gameState, response)
    return response


# choose where to go (escape or go to powerup)
def handle_move(turn_data: GameState, response: PlayerCommand):
    # Implement your move handling logic here
    pass

# choose target (enemy or door)
def choose_target(turn_data: GameState, response: PlayerCommand):
    # Implement your target choosing logic here
    pass
    # return target

def shoot(target:Flame, turn_data: GameState, response: PlayerCommand) -> dict:
    # Implement your shooting logic here
    pass

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=3000)