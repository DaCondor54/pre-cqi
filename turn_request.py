from dataclasses import dataclass
from typing import List, Literal

from common import Position

@dataclass
class Velocity:
    x: float
    y: float


@dataclass
class Player:
    position: Position
    speed: float
    fireCooldown: float  # 0 means can fire
    remainingTicksInRapidFire: int
    remainingTicksInRapidWalk: int
    remainingSuperBullets: int


@dataclass
class Bullet:
    id: str
    position: Position
    velocity: Velocity
    angle: float
    speed: float
    isSuper: bool


@dataclass
class Flame:
    id: str
    hp: float
    position: Position
    velocity: Velocity
    angle: float
    speed: float
    type: Literal['flame', 'campfire']


@dataclass
class SpawnPoint:
    x: float
    y: float
    width: float
    height: float

@dataclass
class MapSize:
    width: float
    height: float

@dataclass
class DebugPoint:
    id: str
    name: str
    position: Position


@dataclass
class MapData:
    size: MapSize  # width/height only; reused type for simplicity
    spawnPoints: List[SpawnPoint]
    seed: int
    debugPoints: List[DebugPoint]


@dataclass
class Item:
    id: str
    type: Literal['nuke', 'rapidfire', 'rapidwalk', 'superbullet']
    position: Position


@dataclass
class Constants:
    flameRadius: float
    bulletRadius: float
    playerRadius: float
    itemRadius: float
    playerDefaultSpeed: float
    rapidWalkMultiplier: float
    rapidFireCooldown: float


@dataclass
class GameState:
    tick: int
    player: Player
    bullets: List[Bullet]
    flames: List[Flame]
    map: MapData
    items: List[Item]
    constants: Constants
