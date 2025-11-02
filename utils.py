from turn_request import *
from turn_response import *
import math

def _as_position(obj):
    if isinstance(obj, Position):
        return obj
    if isinstance(obj, dict):
        if "position" in obj:
            return Position(**obj.get("position", {}))
        return Position(**obj)
    raise TypeError(f"Cannot convert to Position: {type(obj)}")

def euclidean_distance(a, b) -> float:
    pa = _as_position(a)
    pb = _as_position(b)
    dx = pa.x - pb.x
    dy = pa.y - pb.y
    return (dx * dx + dy * dy) ** 0.5


def compute_angle(current_position: Position, target_position:Position):
    dx = target_position.x - current_position.x
    dy = target_position.y - current_position.y
    angle_rad = math.atan2(dy, dx)
    angle_deg = math.degrees(angle_rad)
    return (angle_deg + 360.0) % 360.0
