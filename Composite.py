# Composite
from Component import PackableItem


class Bag(PackableItem):
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def get_weight(self):
        return sum(item.get_weight() for item in self.items)

    def __str__(self):
        content = "\n  ".join(str(item) for item in self.items)
        return f"{self.name} contains:\n  {content}"