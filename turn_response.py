from dataclasses import dataclass
from typing import List, Optional, Literal

from common import Position

@dataclass
class Move:
    direction: float  # 0–360 degrees
    speed: float      # 0–1 float


@dataclass
class DebugPointAction:
    action: Literal['add', 'remove', 'clear']
    name: Optional[str] = None  # not needed for 'clear'
    position: Optional[Position] = None  # not needed for 'clear' or 'remove'


@dataclass
class PlayerCommand:
    move: Move
    fire: Optional[float] = None  # 0–360 degrees, optional
    debugPoints: Optional[List[DebugPointAction]] = None  # optional
