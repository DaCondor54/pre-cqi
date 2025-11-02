from turn_request import *
from turn_response import *

def _as_position(obj):
    if isinstance(obj, Position):
        return obj
    if isinstance(obj, dict):
        if "position" in obj:
            return Position(**obj.get("position", {}))
        return Position(**obj)
    raise TypeError(f"Cannot convert to Position: {type(obj)}")

def _euclidean_distance(a, b) -> float:
    pa = _as_position(a)
    pb = _as_position(b)
    dx = pa.x - pb.x
    dy = pa.y - pb.y
    return (dx * dx + dy * dy) ** 0.5