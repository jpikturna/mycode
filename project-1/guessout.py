#!/usr/bin/env python3

"""Guessout:  Guess the most popular cities for three of the top outdoor sports!"""

def main():
    # Break it down to Hiking, Biking, Climbing
    sports = ["Hiking", "Biking", "Climbing"]

    # Break the sports down into three top cities each
    hikingcities = ["Denver", "Seattle", "San Diego"]
    bikingcities = ["Salt Lake City", "Phoenix", "Bentonville"]
    climbingcities = ["El Paso", "Las Vegas", "Yucca Valley"]

    # Print a "Welcome" statement and list the rules
    print("""
 GUESSOUT
 ========
 Pick a sport and guess which of the top three cities for that sport is number one!
 ========""")

    # Initialize a counter and begin the game!
    counter = 0
    chosensport = input("Choose a sport to play! (Hiking, Biking, Climbing)").title()

    if chosensport == sports[0]:
        while counter < 3:
            chosencity = input("Which of the following three cities is MOST popular for hiking? (Seattle, Denver, San Diego) or ((Q)uit)").title()
            if chosencity == "Denver":
                print("Congratulations! Denver's Rocky Mountain High elevation and close proximity to hundreds of hikes make it a Hiker's Paradise!")
                break
            elif chosencity.lower() == "q":
                print("Thanks for playing! Go be outside!")
                break
            else:
                print("Sorry, try again!")
            counter += 1
        else:
            print("Sorry, the answer was Denver!")
    elif chosensport == sports[1]:
        while counter < 3:
            chosenplace = input("Which of the following three cities is MOST popular for mountain biking? (Salt Lake City, Phoenix, or Bentonville) or ((Q)uit)").title()
            if chosenplace == "Salt Lake City":
                print("Congratulations! You guessed that the Mecca for the LDS is also a site of pilgrimage for mountain bikers!")
                break
            elif chosenplace.lower() == "q":
                print("Thanks for playing! Put on a helmet and get pedaling!")
                break
            else:
                print("Sorry, try again!")
            counter += 1
        else:
            print("Sorry, the answer was Salt Lake City!")
    elif chosensport == sports[2]:
        while counter < 3:
            chosenlocation = input("Which of the following three cities is MOST popular for climbing? (Yucca Valley, Las Vegas, or El Paso?) or ((Q)uit)").title()
            if chosenlocation == "El Paso":
                print("Congratulations! Hueco Tanks located just outside El Paso is home to world-class sandstone bouldering at the border!")
                break
            elif chosenlocation.lower() == "q":
                print("Thanks for playing! Cram your feet into some tiny shoes and climb the side of your building!")
                break
            else:
                print("Sorry, try again!")
            counter += 1
        else:
            print("Sorry, the answer was El Paso!")
    else:
        print("Please enter a valid outdoor sport! (Hiking, Biking, Climbing)")

if __name__ == "__main__":
    main()
