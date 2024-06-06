
# ex1.1: Finding the longest name in the file
with open('names.txt') as f:
    # Read the file, split it into lines, find the longest name, and print it
    print(max(f.read().splitlines(), key=len))

# ex1.2: Calculating the sum of the lengths of all names in the file
with open('names.txt') as f:
    # Read the file, split it into lines, calculate the sum of the lengths of the names, and print it
    print(sum(len(name) for name in f.read().splitlines()))

# ex1.3: Printing the shortest names in the file, each name on a separate line
with open('names.txt') as f:
    # Read the file and split it into lines
    names = f.read().splitlines()
    # Find the minimum length of the names in the list
    min_length = min(len(name) for name in names)
    # Print all names with the minimum length, each on a separate line
    print("\n".join(name for name in names if len(name) == min_length))


# ex1.4: Creating a new file with the lengths of the names in the original file
with open('names.txt') as f, open('name_length.txt', 'w') as out:
    # Read the file and split it into lines, then write the lengths of the names to the new file
    out.write("\n".join(str(len(name)) for name in f.read().splitlines()))

# ex1.5: Printing names of a specific length as input by the user
length = int(input("Enter name length: "))
with open('names.txt') as f:
    # Read the file, split it into lines, and print all names with the specified length
    print("\n".join(name for name in f.read().splitlines() if len(name) == length))
