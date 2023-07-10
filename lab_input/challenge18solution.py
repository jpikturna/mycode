def main():

    #collect user input
    user_name = input("Please enter your name: ")

    #collect day of the week
    week_day = input("What day of the week is it? ")

    #concatenate and print them both
    print("Hello, " + user_name.strip() + "!  Happy " + week_day.strip() + "!")

if __name__ == "__main__":
    main()
