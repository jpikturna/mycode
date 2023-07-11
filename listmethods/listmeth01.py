#!/usr/bin/env python3
proto = ["ssh", "http", "https"]
protoa = ["ssh", "http", "https"]
print(proto)
proto.append("dns") # this line will add "dns" to the end of our list
protoa.append("dns") # this line will add "dns" to the end of our list
print(proto)
proto2 = [ 22, 80, 443, 53 ] # a list of common ports
proto.extend(proto2) # pass proto2 as an argument to the extend method
print(proto)
protoa.append(proto2) # pass proto2 as an argument to the append method
print(protoa)
goobers = ["charlie", "chuck", "charles"]

print(f"I call my dog a lot of names.  My favorites are {goobers[0]}, {goobers[1]}, and, of course, {goobers[2]}")

goobers.insert(2, "CHORLE")

print(goobers)

