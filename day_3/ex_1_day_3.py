with open('day_3.txt', 'r') as file:
    for line in file:
        lenline = len(line)
        break

matrix_list = []
for i in range(lenline-1):
    col_string = ""
    with open('day_3.txt', 'r') as file:
        for line in file:
            col_string += line[i]
    matrix_list.append(col_string)

binary_string_most = ""
binary_string_second = ""
for i in range(len(matrix_list)):
    ones = matrix_list[i].count('1')
    zeros = matrix_list[i].count('0')
    if zeros > ones:
        binary_string_most += "0"
        binary_string_second += "1"
    elif ones > zeros:
        binary_string_most += "1"
        binary_string_second += "0"

print(int(binary_string_most, 2) * int(binary_string_second, 2))