# Implement a class to hold room information. This should have name and
# description attributes.

class Room():
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []

    def addItem(self, array):
        self.items.append(array)
        for i in self.items:
            print(f"the items in the list {i}")

    def __str__(self):
        return f"{self.name}: {self.description}"

# newRoom = Room("chungus", "The land of all chungs")

# newRoom.addItem({"item":"Heavenly Sword"})

# if len(newRoom.items) > 0:
#     for i in newRoom.items:
#         print(f"Each Item itterated: {i}")

# else:
#     print("There are no items in this room!")

# print(newRoom,'The new room with items')

# print(newRoom.addItem({"item":"Heavenly Sword"}), 'the item printed')

