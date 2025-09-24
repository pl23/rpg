class character:
    def __init__(self, name, combat_module):
        self.name = name
        self.combat = combat_module.combat(name, {}) 