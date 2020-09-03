# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room

class Player:
    def __init__(self, name, current_room, item=[]):
        self.name = name 
        self.current_room = current_room
        self.item = item

    def move(self, direction):
        """This should move the player"""
        new_room = self.current_room.get_direction(direction)
        if new_room is not None:
            self.current_room = new_room
            print(self.current_room)
        else:
            print("You cannot move in that direction.")
            print(self.current_room.get_exit())

    def take(self, item):
        self.item.append(item)
        print(f'{self.name} picks up a {item}')
    
    def drop(self, item):
        #print(f'{self.name} drops a {item}')
        del self.item[item]
        
        