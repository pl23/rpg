from . import base as character_base
from .invatory import base as inventory_base
from .combat import base as combat_base

class Player(character_base.character):
    """Player instance class that extends the base character class"""
    
    def __init__(self, name):
        # Initialize base character with combat system
        super().__init__(name, combat_base)
        
        # Add player-specific attributes
        self.inventory = inventory_base.inventory()
        self.level = 1
        self.experience = 0
        self.experience_to_next_level = 100
        self.gold = 0
        
        # Player stats that can be customized
        self.stats = {
            'strength': 10,
            'dexterity': 10,
            'constitution': 10,
            'intelligence': 10,
            'wisdom': 10,
            'charisma': 10
        }
    
    def gain_experience(self, amount):
        """Add experience points to the player"""
        self.experience += amount
        if self.experience >= self.experience_to_next_level:
            self.level_up()
    
    def level_up(self):
        """Level up the player and increase stats"""
        self.level += 1
        self.experience -= self.experience_to_next_level
        self.experience_to_next_level = self.level * 100
        
        # Increase health and combat stats on level up
        self.combat.health += 10
        self.combat.attack_power += 2
        self.combat.defense += 2
        
        print(f"Level up! {self.name} is now level {self.level}!")
    
    def add_gold(self, amount):
        """Add gold to the player"""
        self.gold += amount
    
    def spend_gold(self, amount):
        """Spend gold if the player has enough"""
        if self.gold >= amount:
            self.gold -= amount
            return True
        return False
    
    def get_status(self):
        """Return a dictionary with the player's current status"""
        return {
            'name': self.name,
            'level': self.level,
            'health': self.combat.health,
            'experience': self.experience,
            'gold': self.gold,
            'attack_power': self.combat.attack_power,
            'defense': self.combat.defense,
            'speed': self.combat.speed,
            'magic': self.combat.magic
        }
    
    def display_status(self):
        """Print the player's current status"""
        status = self.get_status()
        print(f"\n=== {status['name']} ===")
        print(f"Level: {status['level']}")
        print(f"Health: {status['health']}")
        print(f"Experience: {status['experience']}/{self.experience_to_next_level}")
        print(f"Gold: {status['gold']}")
        print(f"Attack Power: {status['attack_power']}")
        print(f"Defense: {status['defense']}")
        print(f"Speed: {status['speed']}")
        print(f"Magic: {status['magic']}")