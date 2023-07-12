#!/usr/bin/env python3

"""Alta3 : Conditionals"""

def main ():

    #round counter
    round = 0
    
    # while lool to loop forr-evv-urrr or until we execute break
    while True:
        round = round + 1
        print('Finish the movie title, "Monty Python\'s Life of ______"')

        answer = input("Your guess --> ")

        if answer == 'Brian':
            print('Correct')
            break

        elif round==3:
            print("Sorry, the answer was: Brian.")
            break

        else:
            print("Try again, stupid.")
if __name__ == "__main__":
    main()
