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
==================================================================================
You've always suspected your neighbor was hiding something.
He smells like a slaughterhouse despite claiming he's an accountant.
You saw him dragging a heavy-looking trash bag into his backyard just after sunset.
You're a good person.  You pay taxes.
It's time to investigate.
==================================================================================
⠀⠀⠀⣠⣴⣶⣶⣾⡿⠿⠿⠿⠷⠦⠤⠀⠀⠀⠀⠠⠶⠿⠿⠿⠿⢿⣷⣶⣶⣦⡄⠀⠀⠀
⠀⣠⣾⡿⠛⣁⣤⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣤⡈⠹⣿⣧⡄⠀
⣰⣿⡿⢆⣾⡟⠃⣠⣶⣶⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣶⣦⡄⠘⢻⣇⡸⢿⣷⡆
⣷⣿⡇⣾⣿⡁⣾⣿⡛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⡇⢸⣿⡇⢸⣿⣿
⠘⣿⣿⣿⣷⣾⣿⡏⠁⠠⣶⣆⡀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⡦⠄⠈⢹⣿⣷⣾⣿⣿⡟⠃
⣾⣵⣿⣿⣿⣿⣿⣷⣶⣶⣷⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣷⣶⣶⣾⣿⣿⣿⣿⣿⣿⣧
⠈⠛⢿⣷⡎⠉⠛⠻⠿⢿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⢾⣿⣿⡿⠿⠟⠛⠉⢱⣾⡟⠛⠁
⠀⠀⠀⢹⡿⠁⠀⠀⠀⠈⢻⣿⣿⡇⠀⠀⠀⠀⠀⠀⣸⣿⣿⡯⠁⠀  ⠀⠀⠸⢿⡇⠀⠀⠀
⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠘⣿⣿⣧⡄⢀⣀⣀⡀⣠⣽⣿⡟⠃⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡿⠏⠘⠋⢠⡄⠘⠋⠹⢿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡆⠀⠀⠀⢸⢁⡀⠀⠐⠃⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣷⡆⠀⠀⢸⡀⠀⠐⢴⣷⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢏⣿⡇⠀⠀⠀⠀⢸⣿⡏⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡆⠐⠒⠀⠐⠐⠂⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡅⠀⠀⠀⠀⣜⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡝⠂⠘⠻⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢃⡠⣄⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
==================================================================================
Commands:
go [direction]
get [item]
look 

    '''))

def showStatus():
    """determine the current status of the player"""
    # print the player's current location
    print(crayons.green(f'''
================================================================================
You're anxiously waiting in the {currentRoom}
Inventory:  {inventory}
    '''))
    # check if there's an item in the room, if so print it
    if "item" in rooms[currentRoom]:
        print(crayons.green('You see a ' + rooms[currentRoom]['item']))
    print(crayons.green("================================================================================"))
    

# an inventory, which is initially empty
inventory = []

## A dictionary linking a room to other rooms
rooms = {
             'Hall' : {
                  'north' : 'Deep Hallway',
                  'east'  : 'Lethargy Living Room',
                  'west'  : 'Desolate Dining Room',
                  'desc'  : 'You are standing in a long, dark hallway with peeling wallpaper, stained rugs,\n and zero decoration.\n  It smells like roadkill in here.'
                     },
            'Lethargy Living Room' : {
                  'west' : 'Hall',
                  'desc' : 'There is a TV playing reruns of The Office.\n  Gross.'
                     },
            'Desolate Dining Room' : {
                  'east' : 'Hall',
                  'north' : 'Killing Kitchen',
                  'desc' : 'A thick layer of dust covers the furniture and plateware.\n  The single bulb left working in the chandellier flickers.\n  A single, red-brown streak adorns the west wall of the room.'
                    },
            'Killing Kitchen' : {
                  'east' : 'Deep Hallway',
                  'south'  : 'Desolate Dining Room',
                  'west' : 'Graveyard Garden',
                  'desc' : 'You desperately search the kitchen for any type of weapon.\n  At this point, you would settle for a wooden spoon'
                    },
            'Deep Hallway' : {
                  'south' : 'Hall',
                  'north' : 'Despair Upstairs',
                  'west' : 'Killing Kitchen',
                  'east' : 'Bathroom of Infinite Self-Loathing',
                  'desc' : 'The smell is getting stronger.\n  At first you thought it was the bathroom, but this stench is stronger than an AIRPORT bathroom'
                    },
            'Bathroom of Infinite Self-Loathing' : {
                  'west' : 'Deep Hallway',
                  'item' : 'plunger of destiny',
                  'desc' : 'Okay, so this bathroom is actually pretty nice, which is weird, right?\n  This guy has weird fresh potpourri and goat milk hand soap.\n  You turn to see what has to be the nicest, most ergonomically-designed plunger you have ever laid eyes on.'
                    },
            'Despair Upstairs' : {
                  'north' : 'Deep Hallway',
                  'south' : 'Creepy Closet',
                  'west'  : 'Ghoulish Guestroom',
                  'east'  : 'Master Deadroom',
                  'desc'  : 'You are at the top of the spiral staircase.\n  You are now facing South.\n  The smell is so bad you barely notice a bedroom to the West, a master bedroom to the East, and a weird closet at the end of the hall.'
                    },
            'Goulish Guestroom' : {
                  'east' : 'Despair Upstairs',
                  'desc' : 'The room is completely empty.\n  The closet has no door and the floor is covered with plastic.\n  You feel a sense of impending death for some reason.'
                    },
            'Creepy Closet' : {
                  'north' : 'Despair Upstairs',
                  'item' : 'key',
                  'desc' : 'Through the miasma of general smells, moths, tattered coats, and dusty shoes you see a single key.\n  I dunno, kinda seems important or somethin...'
                    },
            'Master Deadroom' : {
                  'west' : 'Despair Upstairs',
                  'item' : 'Normal Gun',
                  'desc' : 'The smell is unbearable.\n  You can hardly see through your watering eyes and dry heaves.\n  The bed is just a swirled mass of remains like a disgusting nest.\n  You see a discarded police uniform next to the wall.\n  The utility belt still has a 9mm pistol holstered.'
                    },
            'Graveyard Garden' : {
                  'east' : 'Killing Kitchen',
                  'item' : 'Wendigo',
                  'desc' : 'Something wearing your neighbor as a suit is blocking the back gate.\n  It is nearly 8 ft. tall, with preternaturally long limbs and digits.\n  Two burning coals glare at you from inside the Elk(?) skull that functions as its head.\n  The scream it emits when it charges you will scar you for life, however shortened that life might be now.'
                  }
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

    #if they type 'look' first
    if move[0] == 'look':
        print(crayons.green(rooms[currentRoom]['desc']))
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
==================================
Calling it?  I don't blame you.
It's creepy in here...
...anyway, bye!
==================================
        '''))
        break
    # Define how a player can win
    if currentRoom == 'Graveyard Garden' and 'key' not in inventory:
        print(crayons.red(f'''
======================================================================
You see your neighbor standing in the garden... \n
Why is he twitching?  Wh is he covered in... blood? \n
He comes priting at you on all fours.
You try to run.
You fail.
=======================================================================
⠀⢀⣠⣤⣤⣄⡀⠀
⣴⣿⣿⣿⣿⣿⣿⣦
⣿⣿⣿⣿⣿⣿⣿⣿
⣇⠈⠉⡿⢿⠉⠁⢸
⠙⠛⢻⣷⣾⡟⠛⠋
YOU DIED
======================================================================
                    '''))
        break
    elif currentRoom == 'Graveyard Garden' and 'key' in inventory and 'Normal Gun' in inventory:
        print(crayons.red(f'''
========================================================================
You see your neighbor standing in the garden...\n
Why is he twitching?  Why is he covered in... blood? \n
He comes sprinting at you full tilt, so you draw your weapon and fire...
=========================================================================
⠀⢀⣠⣤⣤⣄⡀⠀
⣴⣿⣿⣿⣿⣿⣿⣦
⣿⣿⣿⣿⣿⣿⣿⣿
⣇⠈⠉⡿⢿⠉⠁⢸
⠙⠛⢻⣷⣾⡟⠛⠋
YOU DIED
=========================================================================
            '''))
        break
    elif currentRoom == 'Graveyard Garden' and 'key' in inventory and 'plunger of destiny' in inventory:
        print(crayons.red(f'''
You see your neighbor standing in the garden...\n
Well... he got taller... and grew horns...
He comes sprinting at you on all fours, so you panic and ready the Plunger of Destiny...
You stick the plunger to his weird skull-face!
You rush to the gate, use the key you found and run out into the street!!
CONGRATULATIONS, YOU ESCAPED THE WENDIGO NEXT DOOR!
★ ° . *　　　°　.　°☆ 　. * ● ¸ 
. 　　　★ 　° :. ★　 * • ○ ° ★　 
.　 * 　.　 　　　　　. 　 
° 　. ● . ★ ° . *　　　°　.　°☆ 
　. * ● ¸ . 　　　★ 　° :●. 　 * 
• ○ ° ★　 .　 * 　.　 　　　　　.
 　 ° 　. ● . ★ ° . *　　　°　.　
°☆ 　. * ● ¸ . 　　　★ 　
° :. 　 * • ○ ° ★　 .　 * 　.　 
　★　　　　. 　 ° 　.  . 　    ★　 　　
° °☆ 　¸. ● . 　　★　★ 
° . *　　　°　.　°☆ 　. * ● ¸ . 
★ ° . *　　　°　.　°☆ 　. * ● ¸ 
. 　　　★ 　° :. 　 * • ○ ° ★　 
.　 * 　.　 　★     ° :.☆
You run off into the night...
            '''))
        break
