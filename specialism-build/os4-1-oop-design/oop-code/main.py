class Character:
    def __init__(self, name, health):
        # Keep the name and the health on the object.
        pass

    def take_damage(self, amount):
        # Take amount off the health. Health never goes below 0.
        pass

    def is_alive(self):
        # True while health is above 0.
        pass

    def speak(self):
        # Give back text like: Sam says: Hello
        pass


class Zombie(Character):
    # A Zombie is a Character. It only changes speak.
    # Its speak gives back text like: Ben says: Grr
    pass
