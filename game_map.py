class Room:
    def __init__(self, name, description, exits):
        self.name = name
        self.description = description
        self.exits = exits


def create_world():
    """
    Current world:
        [F]
         |
        [C]
         |
        [W]-[F]
         |   |
        [C] [F]
    """
    world = {
        'welcome': Room(
            "welcome",
            "You are in a forest.",
            {'n': 'clearing', 'e': 'forest2', 's': 'clearing2'}),
        'clearing': Room(
            "clearing",
            "You are in a clearing surrounded by forest.",
            {'s': 'welcome', 'n': 'forest'}),
        'forest': Room(
            "forest",
            "You are in a dense forest.",
            {'s': 'clearing'}),
        'forest2': Room(
            "forest",
            "You are in a dense forest.",
            {'w': 'welcome', 's': 'forest3'}),
        'forest3': Room(
            "forest",
            "You are in a dense forest.",
            {'w': 'welcome'}),
        'clearing2': Room(
            "clearing",
            "You are in a clearing surrounded by forest.",
            {'n': 'welcome'}),
    }

    return world
