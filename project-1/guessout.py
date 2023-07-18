#!/usr/bin/env python3

"""Guessout:  Guess the most popular cities for three of the top outdoor sports!"""

def main():
    #Break it down to Hiking, Biking, Climbing
    sports = ["Hiking", "Biking", "Climbing"]
    
    #Break the sports down into three top cities each
    hikingcities = ["Denver", "Seattle", "San Diego"]
    bikingcities = ["Salt Lake City", "Phoenix", "Bentonville"]
    climbingcities = ["El Paso", "Las Vegas", "Yucca Valley"]

    #Print a "Welcome" statement and list the rules
    print(f"Welcome to Guessout!  In this game you have two chances to  guess which of the top three cities in a sport is number one!")
    
    #initialize a counter and begin the game!
    counter = 0
    chosensport = input("Choose a sport to play! (Hiking, Biking, Climbing)").title()
    
    if chosensport == sports[0]:
        chosencity = input("Which of the following three cities is MOST popular for hiking? (Seattle, Denver, San Diego) or ((Q)uit)").title()
        while counter < 3 and chosencity != hikingcities[0]:
            if chosencity == "Denver":
                print(f"Congratulations!  Denver's Rocky Mountain High elevation and close proximity to hunreds of hikes makes it a Hiker's Paradise!")
            elif chosencity == "Q":
                print("Thanks for playing!  Go be outside!")
            elif counter == 3:
                print("Sorry, DENVER is the answer!")
            else:
                input("Sorry, try again!")
    elif chosensport == sports[1]:
        chosenplace = input("Which of the following three cities is MOST popular for mountain biking? (Salt Lake City, Phoenix, or Bentonville) or ((Q)uit)").title
        while counter < 3 and chosenplace != bikingcities[0]:
            if chosenplace == "Salt Lake City":
                print("Congratulations!  You guessed that the Mecca for the LDS is also a site of pilgrimage for mountain bikers!")
            elif chosenplace == "Q":
                print("Thanks for playing!  Put on a helmet and get pedaling!")
            elif counter == 3:
                print("Sorry, the answer was Salt Lake City!")
            else:
                input("Sorry, try again!")
    elif chosensport == sports[2]:
        chosenlocation = input("Which of the following three cities is MOST popular for moutain biking? (Yucca Valley, Las Vegas, or El Paso?) or ((Q)uit)").title
        while counter < 3 and chosenlocation != climbingcities[0]:
            if chosenlocation == "El Paso":
                print("Congratulations!  Hueco Tanks located just outside El Paso are home to world-class sandstone bouldering at the border!")
            elif chosenlocation == "Q":
                print("Thanks for playing!  Cram your feet into some tiny shoes and climb the side of your building!")
            elif counter == 3:
                print("Sorry, the answer was El Paso!")
            else:
                input("Sorry, try again!")
    else:
        input("Please enter a valid outdoor sport! (Hiking, Biking, Climbing)")

if __name__ == "__main__":
    main()  
