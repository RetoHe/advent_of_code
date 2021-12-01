# create function 
filename = "day_1.txt"
def count_increases(path):
    list_ = open(path).read().split()   # import file as list
    increases = 0                       # create counter

    for i in range(1,len(list_)):       # loop to check if next value is greater
        if int(list_[i]) > int(list_[i-1]):
            increases += 1
        else:
            pass
    return increases      


def main():
    values = count_increases(filename)
    print("There are {} increasing values in the file.".format(values))


if __name__ == "__main__":
    main()



