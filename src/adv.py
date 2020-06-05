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

#tries to move the player in the specified direction 
def try_direction(player, direction):
    # check the player's current location and see if there is 
    # a room in the specified direction
    # if there is, move them there to that room
    # otherwise, a print message saying "we can't go there" and 
    # not move the player

    attribute = direction + '_to'

    # python has a handy method called hasattr
    # which allows us to check if a class has an attribute
    if hasattr(player.location, attribute):
        #this is a valid direction
        # use getattr to fetch the value associated with the attribute
        # update our player's location with the fetched room
        player.location = getattr(player.location, attribute)
    else: 
        print('\n')
        print("There is nothing in that direction!")





# Make a new player object that is currently in the 'outside' room.

player = Player(room['outside'], "Jim")

player.location.addItem({ 'name': "Aphrodites Bow", "desc":"A bow and arrow that can incinerate an opponent or grants you mind control over a player for a fixed time"})


# Write a loop that:
while True:
    # * Prints the current description  and location(the textwrap module might be useful here). 
    print('\n')
    print(player.location)

    # print out list of items if they exist in a room

    if len(player.location.items) > 0:
        print('\n')
        print("Available items in this room:")
        print('\n')
        for i in player.location.items:
            
            print(f"{i['name']}: {i['desc']}") # prints out the name and desc of item

    else:
        print('\n')
        print("There are no items in this room!")

    # * Waits for user input and decides what to do.
    command = input("\nCommand: ").strip().lower().split()
    print(command[0])
    



# if the first letter is get and the last word is item name
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


    
    

    command2 = command[0]

    first_word = command2[0]

    if first_word == 'q':
        break


    # first_char = str(command[0])
    # print(first_char,'the first char')

    if first_word == 'n':
        #move to the north
        try_direction(player, first_word)

    elif first_word == 's':
        # move to the south
        try_direction(player, first_word)
    elif first_word == 'w':
        #move to the west
        try_direction(player, first_word)
    elif first_word == 'e':
        #move to the east
        try_direction(player, first_word)
