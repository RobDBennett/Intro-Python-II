from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
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
#
print("Welcome to the Text Based adventure of walking around some rooms.")
# Make a new player object that is currently in the 'outside' room.
name = input("Please enter your name: ")
newplayer = Player(name=name, current_room=room['outside'])
print(f"\n {newplayer.name} is currently {newplayer.current_room}")
cr = newplayer.current_room
#print(room[cr].name, '\n', room[cr].description)
# Write a loop that:

move_commands = ['n', 'N', 'e', 'E', 'w', 'W', 's', 'S']
selection = "q"

while True:
    cmd = input("Enter the direction you wish to go, or enter Q to quit:")
    if cmd in move_commands:
        newplayer.move(cmd)
    elif cmd in ['q', 'Q']:
        print("Only quitters quit")
        break
    else:
        print("I did not understand that command\n")




#    current_room = newplayer.room
#    print(room[current_room].name, room[current_room].description)
#    selection = input(f"Where does {newplayer.name} wish to go? (n/s/e/w or q to quit).")

        


# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
