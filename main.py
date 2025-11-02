from turtle import distance
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from turn_request import *
from turn_response import *
from utils import _euclidean_distance

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
    response.move.direction = 180
    response.move.speed = 1
    pass

# choose target (enemy or door)
def choose_target(turn_data: GameState, response: PlayerCommand) -> Flame:
    player_position = Position(**turn_data.player.get("position", {}))
    flames = turn_data.flames
    if( not flames ):
        return Flame(position=Position(x=0, y=0), id="", hp=0, velocity=Velocity(x=0,y=0), angle=0, speed=0, type='flame')
    closest_flame = get_closest_flame(player_position, flames)
    return closest_flame

def get_closest_flame(player_position: Position, flames: list[Flame]) -> Flame:
    closest_flame = min(flames, key=lambda f: _euclidean_distance(player_position, f.get("position", {})))
    return closest_flame

def shoot(target:Flame, turn_data: GameState, response: PlayerCommand) -> dict:
    # Implement your shooting logic here
    pass

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=3000, reload=True)