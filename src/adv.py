from room import Room
from player import Player
from os import system, name
from item import Item


# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                     [Item('Lantern', 'Dented, but provides light')]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [Item('Stick', 'A weapon, I guess.')]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [Item('Bird', 'Maybe a meal?')]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [Item('Sand', 'A handful of sand.')]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [Item('Coin', 'A bit of treasure')]),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


print("Welcome to the Text Based adventure of walking around some rooms.")
# Make a new player object that is currently in the 'outside' room.
name = input("Please enter your name: ")
newplayer = Player(name=name, current_room=room['outside'])
print(f"\n {newplayer.name} is currently {newplayer.current_room}")
cr = newplayer.current_room
#print(room[cr].name, '\n', room[cr].description)
# Write a loop that:

move_commands = ['n', 'N', 'e', 'E', 'w', 'W', 's', 'S']

while True:
    cmd = input("Enter the direction you wish to go.\n or enter Q to quit:")
    action = cmd[0:4]
    item = cmd[5:]
    if cmd in move_commands:
        clear()
        newplayer.move(cmd)
    elif cmd in ['q', 'Q']:
        print("Only quitters quit")
        break
    elif cmd in ['i', 'I']:
        if len(newplayer.item) > 0:
            print(f'{newplayer.name} currently has:')
            for x in range(len(newplayer.item)):
                print(f'{newplayer.item[x]}')
        else:
            print(f'{newplayer.name} currently has no items.')
    elif action == 'take':
        item = item.capitalize()
        item_name_list = [i.name for i in newplayer.current_room.item]
        item_index = item_name_list.index(item)
        newplayer.take(newplayer.current_room.item[item_index])
        newplayer.current_room.remove_item(item_index)
    elif action == 'get ':
        item = cmd[4:]
        item = item.capitalize()
        item_name_list = [i.name for i in newplayer.current_room.item]
        item_index = item_name_list.index(item)
        newplayer.take(newplayer.current_room.item[item_index])
        newplayer.current_room.remove_item(item_index)
    elif action == 'drop':
        item = item.capitalize()
        item_name_list = [i.name for i in newplayer.item]
        item_index = item_name_list.index(item)
        newplayer.current_room.add_item(newplayer.item[item_index])
        newplayer.drop(item_index)
        print(f'{newplayer.name} drops a {item}')
    else:
        print("I did not understand that command\n Try n,s,e,w to move.\n Or to take or drop an item, try take item_name.")

