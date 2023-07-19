#!/usr/bin/python3

#python3 -m pip install crayons
import crayons

"""Driving a simple game framework with
   a dictionary object | Alta3 Research"""

def showInstructions():
    """Show the game instructions when called"""
    #print a main menu and the commands
    print(crayons.red('''
ESCAPE FROM YOUR WEIRD NEIGHBOR
================================
Commands:
go [direction]
get [item]
    '''))

def showStatus():
    """determine the current status of the player"""
    # print the player's current location
    print(crayons.green(f'''
===============================
You're anxiously waiting in the {currentRoom}
Inventory:  {inventory}
    '''))
    # check if there's an item in the room, if so print it
    if "item" in rooms[currentRoom]:
        print(crayons.green('You see a ' + rooms[currentRoom]['item']))
    print(crayons.green("================================"))


# an inventory, which is initially empty
inventory = []

## A dictionary linking a room to other rooms
rooms = {
             'Hall' : {
                  'north' : 'Deep Hallway',
                  'east'  : 'Lethargy Living Room',
                  'west'  : 'Desolate Dining Room',
                  'item'  : 'key'
                     },
            'Lethargy Living Room' : {
                  'west' : 'Hall',
                     },
            'Desolate Dining Room' : {
                  'east' : 'Hall',
                  'north' : 'Killing Kitchen'
                    },
            'Killing Kitchen' : {
                  'east' : 'Deep Hallway',
                  'south'  : 'Desolate Dining Room',
                  'item' : 'Wooden Thpoon'
                    },
            'Deep Hallway' : {
                  'south' : 'Hall',
                  'north' : 'Despair Upstairs',
                  'west' : 'Killing Kitchen',
                  'east' : 'Bathroom of Infinite Self-Loathing',
                  'item' :'monster',
                    },
            'Bathroom of Infinite Self-Loathing' : {
                  'west' : 'Deep Hallway',
                  'item' : 'Plunger of Destiny'
                    },
            'Despair Upstairs' : {
                  'north' : 'Deep Hallway',
                  'south' : 'Creepy Closet',
                  'west'  : 'Ghoulish Guestroom',
                  'east'  : 'Master Deadroom'
                    },
            'Goulish Guestroom' : {
                  'east' : 'Despair Upstairs',
                    },
            'Creepy Closet' : {
                  'north' : 'Deep Hallway',
                  'item' : 'House Key',
                    },
            'Master Deadroom' : {
                  'west' : 'Despair Upstairs',
                  'item' : 'Home Owner'
                    },
         }

# start the player in the Hall
currentRoom = 'Hall'

showInstructions()

# breaking this while loop means the game is over
while True:
    showStatus()

    # the player MUST type something in
    # otherwise input will keep asking
    move = ''
    while move == '':  
        move = input('>')

    # normalizing input:
    # .lower() makes it lower case, .split() turns it to a list
    # therefore, "get golden key" becomes ["get", "golden key"]          
    move = move.lower().split(" ", 1)

    #if they type 'go' first
    if move[0] == 'go':
        #check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            #set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
        # if they aren't allowed to go that way:
        else:
            print('You cannot go that way!')

    #if they type 'get' first
    if move[0] == 'get' :
        # make two checks:
        # 1. if the current room contains an item
        # 2. if the item in the room matches the item the player wishes to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            #add the item to their inventory
            inventory.append(move[1])
            #display a helpful message
            print(move[1] + ' got!')
            #delete the item key:value pair from the room's dictionary
            del rooms[currentRoom]['item']
        # if there's no item in the room or the item doesn't match
        else:
            #tell them they can't get it
            print('Can\'t get ' + move[1] + '!')
    if move[0] == 'q' :
        #if the player wants to (q)
        print(crayons.blue('''
================================
Calling it?  I don't blame you.
It's creepy in here...
...anyway, bye!
================================
            '''))

    ## If a player enters a room with a monster
    if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        print(crayons.red('''
⠀⢀⣠⣤⣤⣄⡀⠀
⣴⣿⣿⣿⣿⣿⣿⣦
⣿⣿⣿⣿⣿⣿⣿⣿
⣇⠈⠉⡿⢿⠉⠁⢸
⠙⠛⢻⣷⣾⡟⠛⠋
YOU DIED
            '''))
        break
    ## Define how a player can win
    if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
        print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
        break

