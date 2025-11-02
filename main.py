from turtle import distance
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from turn_request import *
from turn_response import *
from utils import *
import dacite

BULLET_SPEED = 200.0
FLAME_RADIUS = 0
BULLET_RADIUS = 0
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
    gameState = dacite.from_dict(GameState, turn_data)
    BULLET_RADIUS = gameState.constants.bulletRadius
    FLAME_RADIUS = gameState.constants.flameRadius
    response = PlayerCommand(move=Move(direction=0.0, speed=0.0), debugPoints=[])
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
    player_position = turn_data.player.position
    flames = turn_data.flames
    if( not flames ):
        return get_default_target(turn_data)
    closest_flames = sort_flames_by_distance(player_position, flames)
    for flame in closest_flames:
        if (not is_flame_dying_soon(flame, turn_data.bullets)):
            return flame
    return closest_flames[0]

def get_closest_flame(position: Position, flames: list[Flame]) -> Flame:
    closest_flame = min(flames, key=lambda f: euclidean_distance(position, f.position))
    return closest_flame

def sort_flames_by_distance(player_position: Position, flames: list[Flame]) -> list[Flame]:
    return sorted(flames, key=lambda f: euclidean_distance(player_position, f.position))

def is_flame_dying_soon(flame: Flame, bullets: list[Bullet]) -> bool:
    hp = flame.hp
    for bullet in bullets:
        
        # if hit:  hp -= 1 -> if hp <=0 return True
        continue
    
    return False

def get_closest_bullet_to_flame(flame: Flame, bullets: list[Bullet]) -> Bullet | None:
    if not bullets:
        return None
    closest_bullet = min(bullets, key=lambda b: euclidean_distance(flame.position, b.position))
    return closest_bullet
def get_closest_flame(player_position: Position, flames: list[Flame]) -> Flame:
    closest_flame = min(flames, key=lambda f: euclidean_distance(player_position, f.position))
    return closest_flame

def get_default_target(turn_data: GameState) -> Flame:
    spawn = turn_data.map.spawnPoints[0]
    spawn_position = Position(x=spawn.x + spawn.width / 2, y=spawn.y + spawn.height / 2)
    return Flame(position=spawn_position, id="", hp=0, velocity=Velocity(x=0,y=0), angle=0, speed=0, type='flame')

def shoot(target:Flame, turn_data: GameState, response: PlayerCommand):
    player_position = turn_data.player.position
    target_position = target.position
    dT = euclidean_distance(player_position, target_position) / BULLET_SPEED
    prediction = compute_end_position(target_position, target.velocity, dT)
    response.fire = compute_angle(player_position, prediction)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=3000, reload=True)