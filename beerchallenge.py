def bottles_of_beer(num_lines):
    for i in range(num_lines, 0, -1):
        print(f"{i} bottles of beer on the wall, {i} bottles of beer.")
        print(f"Take one down, pass it around, {i-1} bottles of beer on the wall.")
        print()

num_lines = int(input("Enter the number of lines: "))
bottles_of_beer(num_lines)

