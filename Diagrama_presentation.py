#           +------------------+
#           |   PackableItem   |  (Component)
#           +------------------+
#           | + get_weight()   |
#           +------------------+
#                   ▲
#                   │
#    +--------------+--------------+
#    |                             |
# +----------------+      +----------------+
# |    Item       |      |     Bag        |   (Composite)
# +----------------+      +----------------+
# | - name        |      | - name          |
# | - weight      |      | - items (list)  |
# +----------------+      +----------------+
# | + get_weight()|      | + add_item()    |
# |               |      | + get_weight()  |
# +---------------+      +----------------+
#                                  ▲
#                                  │
#         +----------------------------------+
#         |              LargeBag           |  (Concrete Composite)
#         +----------------------------------+
#         | - "Healthy Food Bag"            |
#         | - "Corn"                         |
#         +----------------------------------+
#                       ▲
#                       │
#      +----------------------------------+
#      |        HealthyFoodBag         |
#      +----------------------------------+
#      | - "Bread"                       |
#      | - "Cheese"                      |
#      | - "Snacks Bag"                   |
#      +----------------------------------+
#                           ▲
#                           │
#           +--------------------------------+
#           |          SnacksBag           |
#           +--------------------------------+
#           | - "Bamba"                      |
#           | - "Bissli"                     |
#           | - "Marshmallow"                |
#           | - "Water Bottle"               |
#           +--------------------------------+
