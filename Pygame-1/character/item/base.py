


class item:
    def __init__(self, item_index = None):
        self.item = {}
        self.item["item_index"]
        if item_index == None:
            self.item["item_index"] = 0
        else:
            self.item["item_index"] = item_index
        self.item["name"] = "item"
        self.item["description"] = None
        self.item["value"] = 0
        self.item["weight"] = 0
        self.item["type"] = None
        self.item["materials"] = []
        self.item["quantity"] = 0
        self.item["stackable"] = False
        
class base_materials(item):
    def __init__(self, item_index = None):
        super().__init__(item_index)
        self.item["type"] = "material"
        self.item["material"] = None
        self.item["value"] = 0
        self.item["weight"] = 0
        self.item["quantity"] = 0
        self.item["stackable"] = True
    
class weapon(item):
    def __init__(self, item_index = None):
        super().__init__(item_index)
        self.combat_stats = {}
        self.item["type"] = "weapon"
        self.combat_stats["damage"] = 0
        self.combat_stats["range"] = 0
        self.combat_stats["accuracy"] = 0
        self.combat_stats["weapon_type"] = None
        self.combat_stats["weapon_class"] = None
        self.combat_stats["weapon_subclass"] = None
        self.combat_stats[""] = None
        
        
        