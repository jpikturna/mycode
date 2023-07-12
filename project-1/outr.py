#!/usr/bin/env python3

"""Outr: A Service to Find Your Outdoor Destination"""

def main():
    #create a big, fat dictionary named destinations and fill with outdoor sports subdictionaries
    #fill the subdictionaries with city keys with a list of "whys" as values
    destinations= {
    "Hiking":
        {"Denver": "Denver's Rocky Mountain High elevation and close proximity to many hikes makes it a Hiker's paradise!",
        "Seattle": "Seattle's famously long summer light hours mean its many accessible mountains and beaches are open longer!",
        "San Diego": "San Diego's year-round balmy weather and gorgeous views make is a winter getaway for Hikers!"},
    "Biking":
        {"Salt Lake City": "The Dry State Capitol boasts hundreds of miles of singletrack and FIVE bike parks within an hour drive",
        "Phoenix": "Be sure to visit Arizona's Capitol just after monsoon season to enjoy a desert bloom on ride through the endless back country",
        "Bentonville": "Did you have to google Bentonville to figure out where it was?  I bet you did.  It's in Arkansas and it has in-town trails and a humongous bike park"},
    "Climbing":
        {"El Paso": "Thanks to the local 'Hueco Tanks', El Paso is home to world-class andstone bouldering at the border",
        "Las Vegas": "Alex Honnold's current city of residence, Las Vegas is home to over 2,000 climbing routes at Red Rock, alone!",
        "Yucca Valley": "Nestled neatly in the part of California that isn't constantly on fire, Yucca Valley sits next to Joshua Tree, a National Park with over 5000 routes!"}
                }
    print("Welcome to Outr! Let us help you find an outdoorsy city you might* like")
    user_sport= input("Do you like: Hiking, Biking, or Climbing?")
    
    




if __name__ == "__main__":
    main()
