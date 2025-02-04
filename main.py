# Creating the packing setup
from Composite import Bag
from Leaf import Item

large_bag = Bag("Large Bag")
healthy_food_bag = Bag("Healthy Food Bag")
snacks_bag = Bag("Snacks Bag")

# Creating individual items
bread = Item("Bread", 0.5)
cheese = Item("Cheese", 0.3)
water_bottle = Item("Water Bottle", 1.0)
corn = Item("Corn", 0.4)
bamba = Item("Bamba", 0.2)
bissli = Item("Bissli", 0.2)
marshmallow = Item("Marshmallow", 0.3)

# Constructing the hierarchy
snacks_bag.add_item(bamba)
snacks_bag.add_item(bissli)
snacks_bag.add_item(marshmallow)
snacks_bag.add_item(water_bottle)

healthy_food_bag.add_item(bread)
healthy_food_bag.add_item(cheese)
healthy_food_bag.add_item(snacks_bag)

large_bag.add_item(healthy_food_bag)
large_bag.add_item(corn)

# Display the setup
print(large_bag)
print(f"Total weight: {large_bag.get_weight()} kg")