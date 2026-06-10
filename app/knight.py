class Knight:
    def __init__(
        self,
        name: str,
        power: int,
        hp: int,
        armour: list,
        weapon: dict,
        potion: dict,
    ) -> None:
        self.name = name
        self.hp = hp
        self.protection = sum(
            piece["protection"] for piece in armour
        )
        self.power = power + weapon["power"]
        if potion is not None:
            for stat, value in potion["effect"].items():
                setattr(self, stat, getattr(self, stat) + value)

    def take_hit(self, enemy_power: int) -> None:
        self.hp = max(0, self.hp - (enemy_power - self.protection))
