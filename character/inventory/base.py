class inventory:
    def __init__(self,):
        self.items = {}
    def add_item(self, item):
        self.items[item.name] = item