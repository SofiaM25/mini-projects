class Weapon:
    def __init__(self, name: str, weapon_type: str, damage: int, value: int) -> None:
        self.name = name
        self.weapon_type = weapon_type
        self.damage = damage
        self.value = value


iron_sword = Weapon(name="Iron sword", weapon_type="sharp", damage=18, value=15)
short_bow = Weapon(name="Short bow", weapon_type="ranged", damage=17, value=10)
knife = Weapon(name="Knife", weapon_type="combat", damage=5, value=5)

