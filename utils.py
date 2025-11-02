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

def compute_end_position(position: Position, velocity: Velocity, delta_time:float)->Position:
    delta = Position(velocity.x * delta_time, velocity.y *delta_time)
    return Position(position.x + delta.x, position.y + delta.y)

def will_hit(bullet:Bullet, flame:Flame, bullet_radius:float, flame_radius:float)->bool:
    dx, dy = bullet.position.x - flame.position.x, bullet.position.y - flame.position.y
    dvx, dvy = bullet.velocity.x - flame.velocity.x, bullet.velocity.y - flame.velocity.y
    r = bullet_radius + flame_radius

    a = dvx**2 + dvy**2
    b = 2 * (dx * dvx + dy * dvy)
    c = dx**2 + dy**2 - r**2

    if a == 0:  # same velocity → static test
        return c <= 0, 0.0

    disc = b*b - 4*a*c
    if disc < 0:
        return False  # never collide

    sqrt_disc = math.sqrt(disc)
    t1 = (-b - sqrt_disc) / (2*a)
    t2 = (-b + sqrt_disc) / (2*a)

    # pick earliest non-negative time
    return any(t >= 0 for t in (t1, t2))
    