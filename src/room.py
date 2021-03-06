# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item


class Room:
    def __init__(self, name, description, item=[]):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.item = item

    def __repr__(self):
        returnString = f"--------\n\n{self.name}\n\n  {self.description}\n\n----------"
        returnString += f'\n\n[{self.get_exit()}]\n\n'
        return returnString

    def __str__(self):
        if len(self.item) > 0:
            for x in range(len(self.item)):
                print(f'There is a {self.item[x]} here.')
        return f'Room: {self.name} \n Description: {self.description} \n'

    def get_direction(self, direction):
        if direction in ['n', 'N']:
            return self.n_to
        elif direction in ['s', 'S']:
            return self.s_to
        elif direction in ['w', 'W']:
            return self.w_to
        elif direction in ['e', 'E']:
            return self.e_to
        else:
            return None
    
    def get_exit(self):
        exits = ['Only available directions are: ']
        if self.n_to is not None:
            exits.append('n')
        if self.s_to is not None:
            exits.append('s')
        if self.w_to is not None:
            exits.append('w')
        if self.e_to is not None:
            exits.append('e')
        return " ".join(exits)

    def remove_item(self, item):
        del self.item[item]
    
    def add_item(self, item):
        self.item.append(item)
