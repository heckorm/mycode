def sing_bottles_of_beer(starting_bottles):
    for i in range(starting_bottles, 0, -1):
        if i == 1:
            print(f"{i} bottle of beer on the wall, {i} bottle of beer.")
            print("Take one down and pass it around, no more bottles of beer on the wall.")
        elif i == 2:
            print(f"{i} bottles of beer on the wall, {i} bottles of beer.")
            print(f"Take one down and pass it around, {i-1} bottle of beer on the wall.")
        else:
            print(f"{i} bottles of beer on the wall, {i} bottles of beer.")
            print(f"Take one down and pass it around, {i-1} bottles of beer on the wall.")
        print()  # Add a blank line for better readability

    print("No more bottles of beer on the wall, no more bottles of beer.")
    print(f"Go to the store and buy some more, {starting_bottles} bottles of beer on the wall.")

if __name__ == "__main__":
    try:
        starting_bottles = int(input("Enter the starting number of bottles: "))
        if starting_bottles < 1:
            raise ValueError("Please enter a positive integer greater than 0.")
        sing_bottles_of_beer(starting_bottles)
    except ValueError as e:
        print(f"Error: {e}")

