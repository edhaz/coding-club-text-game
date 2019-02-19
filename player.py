import random


class Player:
    def __init__(self, name, health, bag, world):
        self.name = name
        self.world = world
        self.room = world['welcome']
        self.health = health
        self.bag = bag

    def look(self):
        print(self.room.description)
        print('Exits:', [i.upper() for i in self.room.exits])

    def move(self, direction):
        if direction not in self.room.exits:
            print(random.choice(["Cannot move in that direction!", "The way is blocked!"]))
            return
        new_room_name = self.room.exits[direction]
        print(f"Moving to {self.world[new_room_name].name}.")
        self.room = self.world[new_room_name]

    @staticmethod
    def help():
        print("Commands:")
        print("'look': see where you are.")

    def attack(self):
        print("You lash out at nothing in particular.")
