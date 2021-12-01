# create function 
filename = "day_1.txt"
# Get Sliding Window List
def get_sliding_window_list(path):
    list_ = open(path).read().split()
    window_sums = []
    increases = 0
    for i in range(len(list_)-2):
        win_sum = int(list_[i]) + int(list_[i+1]) + int(list_[i+2])
        window_sums.append(win_sum)

    return window_sums

# Count Increasing Values
def count_increases(num_list):
    increases = 0                       # create counter

    for i in range(1,len(num_list)):       # loop to check if next value is greater
        if int(num_list[i]) > int(num_list[i-1]):
            increases += 1
        else:
            pass
    return increases 

def main():
    numbers = get_sliding_window_list(filename)
    values = count_increases(numbers)
    print("There are {} increasing values in the file.".format(values))
    #print(values)

if __name__ == "__main__":
    main()
