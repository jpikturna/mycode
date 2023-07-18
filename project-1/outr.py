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
    
    if user_sport == "Hiking":
        print(f"The top three Hiking cities are {destinations["Hiking"][0]}, {destinations["Hiking"][1]}, and {destinations["Hiking"][2]}!")
        hiking_city = input("Which city do you want to learn more about (Denver, Seattle, San Diego)?").capitalize()
        if hiking_city == "Denver":
            print(destinations[0][0].value())
        elif hiking_city == "Seattle":
            print(destinations[0][1].value())
        else:
            print(destinations[0][2].value())
    elif user_sport == "Biking":
        print(f"The top three Biking cities are {destinations[1][0]}, {destinations[1][1]}, and {destinations[1][2]}!")
        biking_city = input("Which city you you want to learn more about (Salt Lake City, Phoenix, or Bentonville)?").capitalize()
        if biking_city == "Salt Lake City":
            print(destinations[1][0].value())
        elif biking_city == "Phoenix":
            print(destinations[1][1].value())
        else:
            print(destinations[1][2].value())
    elif user_sport == "Climbing":
        print(f"The top three Climbing cities are {desinations[2][0]}, {destinations[2][1]}, and {destinations[2][2]}!")
        climbing_city = input("Which city would you want to learn more about (El Paso, Las Vegas, Yucca Valley)?")


if __name__ == "__main__":
    main()
