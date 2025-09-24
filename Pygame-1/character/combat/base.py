class combat:
    def __init__(self, name, equiped_items):
        self.name = name
        self.equped_items = equiped_items
        self.health = 100
        self.attack_power = 10
        self.defense = 10
        self.speed = 10
        self.magic = 10
        
    def attack(self, target):
        target.combat.update_health(self.attack_power)

    def update_health(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            print(f"{self.name} has been defeated!")
    