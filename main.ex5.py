def check_id_valid(id_number):
    # Check if a given ID number is valid based on the Luhn algorithm.

    id_str = str(id_number)
    # Check if the ID number is 9 digits long
    if len(id_str) != 9:
        return False

    total = 0
    for i, digit in enumerate(id_str):
        digit = int(digit)
        # Double every second digit and sum the digits if necessary
        if i % 2 == 0:
            total += digit
        else:
            digit *= 2
            if digit > 9:
                digit = digit // 10 + digit % 10
            total += digit

    # Check if the total modulo 10 is 0
    return total % 10 == 0


class IDIterator:
    # Iterator class to generate valid ID numbers starting from a given number.

    def __init__(self, id_number):
        self.id_ = id_number
        self.current_id = id_number

    def __iter__(self):
        return self

    def __next__(self):
        # Stop the iteration if the current ID exceeds the maximum value
        if self.current_id > 999999999:
            raise StopIteration
        # Find the next valid ID number
        while not check_id_valid(self.current_id):
            self.current_id += 1
        id_to_return = self.current_id
        self.current_id += 1
        return id_to_return


def id_generator(id_number):
    # Generator function to yield valid ID numbers starting from a given number.

    current_id = id_number
    # Yield valid ID numbers until the maximum value is reached
    while current_id <= 999999999:
        if check_id_valid(current_id):
            yield current_id
        current_id += 1


def main():
    # Main function to prompt the user for input and print valid ID numbers using either an iterator or a generator.

    id_input = int(input("Enter ID: "))
    iterator_or_generator = input("Generator or Iterator? (gen/it)? ")

    if iterator_or_generator == "it":
        # Use the IDIterator class to generate valid ID numbers
        iterator = IDIterator(id_input)
        for _ in range(10):
            print(next(iterator))
    elif iterator_or_generator == "gen":
        # Use the id_generator function to generate valid ID numbers
        generator = id_generator(id_input)
        for _ in range(10):
            print(next(generator))


if __name__ == "__main__":
    main()
