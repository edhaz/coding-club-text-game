import game_map
from player import Player


def welcome():
    print("Welcome to your world.")
    name = input("Enter your name: ")
    new_player = Player(name, 100, [], world)
    print(f"Greetings {name}, you may enter.")
    print("Type 'look' to have a look around.")
    return new_player


if __name__ == "__main__":
    world = game_map.create_world()
    player = welcome()
    while True:
        command = input('>> ')
        command = command.lower()
        if command in {'n', 'e', 's', 'w'}:
            player.move(command)
        elif command in {'help', 'look', 'attack'}:
            action = getattr(player, command)
            action()
        else:
            print('Invalid command')
