file = "day_2.txt"

def get_direction_values(filename):
    horizontal = 0
    depth = 0
    aim = 0

    a_file = open("day_2.txt")
    for line in a_file:
        key, value = line.split()
        if key == "forward":
            horizontal += int(value)
            depth += aim * int(value)

        elif key == "down":
            #depth += int(value)
            aim += int(value)
        elif key == "up":
            #depth -= int(value)
            aim -= int(value)
        else:
            print("Error")
    return horizontal * depth

def main():

    direction = get_direction_values(file)
    print("The position of the boat is {}.".format(direction))


if __name__ == "__main__":
    main()