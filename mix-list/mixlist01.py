#!/usr/bin/env python3

import random

my_list = [ "192.168.0.5", 5060, "UP" ]

print("The first item in the list (IP): " + my_list[0] )

print("The second item in the list (port): " + str(my_list[1]) )

print("The last item in the list (state): " + my_list[2] )

# display only the IP addresses to the screen.
iplist = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]

# example 1 - add up the strings
print("IP addresses: " + iplist[3] + ", and " + iplist[4])

# example 2 - use the comma separator
print("IP addresses:", iplist[3], ", and", iplist[4])

# example 3 - use an 'f-string'
print(f"IP addresses: {iplist[3]}, and {iplist[4]}")

# CHALLENGE LAB 31

wordbank= ["indentation", "spaces"]

tlgstudents= ['Albert', 'Anthony', 'Brenden', 'Craig', 'Deja', 'Elihu', 'Eric', 'Giovanni', 'James', 'Joshua', 'Maria', 'Mohamed', 'PJ', 'Philip', 'Sagan', 'Suchit', 'Meka', 'Trey', 'Winton', 'Xiuxiang', 'Yaping']

# append integer into wordbank list

wordbank.append(4)

num = int(input("Please enter an integer between 0 and 20>"))

weakest_link = tlgstudents[num]

print(weakest_link + " always uses " + str(wordbank[2]) + " " + str(wordbank[1]) + " to indent.")

#Alternate Version

print(f"{weakest_link} always uses {wordbank[2]} {wordbank[1]} to indent.")

name = random.choice(tlgstudents)
print (f"{name}")
