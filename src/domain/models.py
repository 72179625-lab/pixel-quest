from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class Item:
    id: str
    name: str
    item_type: str  # ej: "weapon", "potion", "armor"
    value: int

@dataclass
class Player:
    id: str
    name: str
    health: int = 100
    max_health: int = 100
    level: int = 1
    inventory: List[Item] = field(default_factory=list)

    def is_alive(self) -> bool:
        return self.health > 0

    def take_damage(self, damage: int) -> None:
        self.health = max(0, self.health - damage)

    def heal(self, amount: int) -> None:
        self.health = min(self.max_health, self.health + amount)