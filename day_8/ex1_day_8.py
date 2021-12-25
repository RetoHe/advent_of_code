output = [x.split('|')[1].rstrip('\n') for x in open('day_8.txt', 'r').readlines()]

count = {}

for x in output:
    for digits in x.split(' '):
        number_of_digits = len(digits)
        if number_of_digits in count:
            count[number_of_digits] += 1
        else:
            count[number_of_digits] = 1

print(count[2] + count[3] + count[4] + count[7])