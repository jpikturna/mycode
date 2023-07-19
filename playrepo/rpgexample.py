#!/usr/bin/python3

# standard lib
from random import randint
import sys
import os

# python3 -m pip install dice
import dice

#list of monsters
bestiary = [{'name' : 'goblin', 'health' : 10, 'damage' : '1d5'},
            {'name' : 'orc', 'health' : 15, 'damage' : '1d6'},
            {'name' : 'ogre', 'health' : 20, 'damage' : '1d10'}]
armory = {'sword': {'damage': '1d12'}}
spell_lookup = {'fireball': {'damage': '4d6'}}
player_health = 25
inventory = []
spellbook = []

def combat():
    monster_ID= randint(0,2)

    global player_health, inventory, armory, bestiary
    round = 1
    monster_health = bestiary[monster_ID]['health']

    print(f"A ferocious {bestiary[monster_ID]['name']} approaches! COMBAT HAS BEGUN!\n")
    while True:
        print(f"ROUND {round}")
        print("Player Health: [" + str(player_health) + "]")
        print("Monster Health: [" + str(monster_health) + "]")

        print("Type: RUN, CAST [spell], or USE [weapon]") # gotta write code for cast
        move = input().lower().split() # converts move into a lower-case list to deal with each item in list separately
        monster_damage = sum(dice.roll(bestiary[monster_ID]['damage']))
        print("\n=========================")


        if move[0] == 'use': #
            if move[1] in inventory: # checks if weapon is in your inventory
                player_damage = dice.roll(armory[move[1]]['damage'])
                print(f"You hit a {bestiary[monster_ID]['name']} for {player_damage} damage!")
            if move[1] not in inventory:
                print(f"There is no {move[1]} in your inventory!")

        if move[0] == 'cast': #
            if move[1] in spellbook: # checks if spell is in your spellbook
                if move[1].lower() == 'fireball':
                    player_damage = sum(dice.roll(spell_lookup[move[1]]['damage']))
                    print(f"Summoning eldritch forces, you scorch the {bestiary[monster_ID]['name']} for {player_damage} damage!")
            if move[1] not in spellbook:
                print(f"You don't know the {move[1]} spell!")

        if move[0] == 'run': #
            escape_chance= randint(1,10) #+ player_speed # if I set this variable later, here's where it would work

            if escape_chance >= 10:
                print("You make a flawless escape!")
                break
            if escape_chance >= 5:
                print("You expose your back as you turn and flee- the monster takes advantage.")
                print(f"A {bestiary[monster_ID]['name']} hits you for {monster_damage} damage!")
                player_health -= int(monster_damage)
                if player_health >= 1:
                    print("You managed to escape.")
                    break
                if player_health < 1:
                    print("You have been slain.")
                    print("\nGAME OVER")
                    sys.exit()
            if escape_chance >= 0:
                print("The monster out-maneuvers you and attacks! You do not escape.")

        try:
            monster_health -= int(player_damage)
        except:
            pass
        if monster_health <= 0:
            print(f"The {bestiary[monster_ID]['name']} lies dead. You are victorious!\n")
            break

        print(f"A {bestiary[monster_ID]['name']} hits you for {monster_damage} damage!")
        print ("=========================\n")
        round += 1
        player_health -= int(monster_damage)

        if player_health <= 0:
            print("You have been vanquished! You are dead.")
            sys.exit()

def showInstructions():
    print('''
DEMO RPG GAME
OBJECTIVE: Collect spells and weapons- fight and survive!
--------
Actions:
    GO [north, south, east, west, up, down]
    GET [item, spell]
    USE [item, spell]
    LOOK
    INV/INVENTORY

Type 'help' at any time! Type 'q' to quit!''')

def playerinfo():
#    print('')
#    print('YOU ARE IN THE ' + currentRoom + '.')
    print('=================================')
    print('Inventory :', str(inventory))
    print('Spells :', str(spellbook))
    print('=================================')


def showStatus(): # display the player's status
 #   if 'desc' in rooms[currentRoom]:
 #       print(rooms[currentRoom]['desc'])
    if 'item' in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'] + rooms[currentRoom]['item_status'] + '.')
    if 'spell' in rooms[currentRoom]:
        print('You see a magic scroll. On the ribbon it says "' + rooms[currentRoom]['spell'] + '".')
#    print('=================')

def spellreceive(incantation):
 #   print("You received a new spell scroll. Be careful... magic is dangerous!")
 #   incantation = input("Create the magic word to summon your spell! >")
 #   if incantation not in spells:
        print("\nA pentagram illuminates beneath your feet as an unnatural wind sweeps your hair.")
        print("The spell has been successfully added to your spellbook. Be careful... magic is dangerous!")

def random_encounter():
    if ((int(rooms[currentRoom]['randenc'])) + 5) >= 10:
        combat()

rooms = {
        'HALL' : {
            'south' : 'KITCHEN',
            'east' : 'DINING ROOM',
            'up' : 'UPPER HALL',
            'item' : 'sword',
            'item_status' : ' inside of a display case. It is unlocked',
            'randenc' : '20',
            'desc' : 'You are in the hall of a large, decrepit house. The walls are blackened from some ancient fire. You get the feeling you are being watched. To the east is a dusty dining room. South is the kitchen... Maybe it was a trick of the light but you thought you saw something moving in there. There is also a very old staircase that leads to an upper floor.',
            'compass' : 'You see that you can go south or east from here. You also see a rickety staircase leading to an upstairs landing.'
            },
        'UPPER HALL' : {
            'down' : 'HALL',
            'east' : 'BEDROOM',
            'randenc' : '0',
            'desc' : 'You arrive at the upstairs landing. The hall splits in two directions from the stairs. You look west and most of the roof has caved in blocking any progression. To the east you see a small amount of light.',
            'compass' : 'You see you can go back down the stairs or go east.'
            },
        'BEDROOM' : {
            'west' : 'UPPER HALL',
            'randenc' : '0',
            'item' : 'key',
            'item_status' : ' amongst the dust',
            'desc' : 'You are in a nicely furnished bedroom. You could imagine living here if it were not for the thick layer of dust. You see the light was coming from a slit in the curtains over the window. Looking out you can see a shed in a yard. Looking more closely, you see there are footprints in the dust that lead toward the bed. A lot of movement has taken place in one area. Following the footprints, you kneel down and look under that bed.',
            'compass' : 'You can go back west to the Upper Hall.'
            },
        'KITCHEN' : {
            'north' : 'HALL',
            'randenc' : '2',
            'down' : 'BASEMENT',
            'desc' : 'You are in what was once a kitchen. Nests made of human bones are draped across every countertop. There is a large hole in the floor. Where it leads you have no idea.',
            'compass' : 'You see that you can go north from here, or you can leap down into the large hole.'
            },
        'BASEMENT' : {
            'up': 'KITCHEN',
            'spell' : 'fireball',
            'desc' : 'You are in a stinking basement with an earthen floor. You can\'t even see your hand in front of your face. You are likely to be eaten by a grue.',
            'randenc' : '1',
            'compass': 'You see the large hole above you. It does not look like there are any other ways to move.'
            },
        'DINING ROOM' : {
            'west' : 'HALL',
            'south' : 'GARDEN',
            'north' : 'PANTRY',
            'east' : 'BACKYARD',
            'desc' : 'You are in the dining room. The table is set for an elegant party but is covered a blanket of dust. Sleeping bats cling to the chandelier.',
            'randenc' : '0',
            'item' : 'potion',
            'item_status' : ' hiding among the bottles of wine. It is cherry red in color',
            'compass' : 'You see to the north is a dark pantry. To the south lies a garden. West brings you back to the Hall. To the east you see a door that leads to dismal yard.'
            },
        'GARDEN' : {
            'north' : 'DINING ROOM',
            'randenc' : '0',
            'desc' : 'You are in an inclosed courtyard garden. All around are high stone walls, too smooth to climb. Maybe if you had a ladder....',
            'compass' : 'You see you can go north to the Dining Room.'
            },
        'PANTRY' : {
            'south' : 'DINING ROOM',
            'desc' : 'You are in a very small pantry. What once were shelves full of delicious food are now full of moldy leftovers. And dust.',
            'compass': 'You can see no other exits except the way you came.',
            'randenc' : '0',
            'item' : 'cookie'
            },
        'BACKYARD' : {
            'west' : 'DINING ROOM',
            'east' : 'SHED',
            'desc' : 'You are in a backyard area. It is overgrown and full of weeds. There is a dead tree in one corner with gnarled branches. Ravens sit in the branches cawing at the sky. You also see a dilapidated shed.',
            'randenc' : '0',
            'compass' : 'You can move east to the shed, but you need a key to unlock the door. Or you can move west to the Dining Room.'
            },
        'SHED' : {
            'west' : 'BACKYARD',
            'item' : 'ladder',
            'item_status' : ' hanging on the far wall',
            'randenc' : '0',
            'desc' : 'You are in tool shed that is so old and full of holes you wonder why you even needed a key to enter. Various garden tools are neatly arranged around the walls and on shelves; they are all showing signs of rust and disuse.',
            'comapss' : 'You can only return west to the yard.'
            }
        }

currentRoom = 'HALL'   # player start location

os.system('clear') # start game with a fresh screen
showInstructions()     # show instructions to the player

while True:   # MAIN INFINITE LOOP
    playerinfo()
    showStatus()
    # ask the player what they want to do
    move = ''
    while move == '':
        move = input('>') # so long as the move does not
        # have a value. Ask the user for input

    move = move.lower().split() # make everything lower case because directions and items require it, then split into a list
    os.system('clear') # clear the screen
    if move[0] == 'go':
        if move[1] in rooms[currentRoom]:
            currentRoom = rooms[currentRoom][move[1]]
            if 'desc' in rooms[currentRoom]:
                print(rooms[currentRoom]['desc'])
            random_encounter()
            # if YES that direction exists, then assign your new current room to the VALUE of the key the user entered
        else:
            print("YOU CAN'T GO THAT WAY!")
    if move[0] == 'use':
        if move[1].lower() == 'potion' and 'potion' in inventory:
            print("You drink from the potion. Your health has been restored!")
            print("Your potion magically refills itself! Handy!")
            player_health = 25
    if move[0] == 'get':
        if 'item' in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            inventory += [move[1]] # add item to inv
            print(move[1].capitalize() + ' received!') # msg saying you received the item
            del rooms[currentRoom]['item'] # deletes that item from the dictionary
        elif 'spell' in rooms[currentRoom] and move[1] in rooms[currentRoom]['spell']:
                spellreceive('spell')
                spellbook += [move[1]]  # add spell to spells
                del rooms[currentRoom]['spell']
        else:
            print('YOU CANNOT GET ' + (move[1].upper()) + '!')

    if move[0] == 'look':
        if 'compass' in rooms[currentRoom]:
            print(rooms[currentRoom]['compass']) # print the compass directions
        else:
            print('You can\'t see anything.')

    elif move[0] == 'help':
        showInstructions()

    elif move[0] in ['q', 'quit]']:
        print("Are you sure you want to quit? Yes/No")
        quit_query = input('>')
        if quit_query.lower() in ['y', 'yes']:
            print("Thanks for playing!")
            sys.exit()
        else:
            pass

    ## Define how a player can win
    if currentRoom == 'GARDEN' and 'ladder' in inventory:
        print('You escaped the house, but just barely. YOU WIN!! ....Until next time.' )
        break
