with open("day_9.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]
#lines = ['2199943210', '3987894921', '9856789892', '8767896789', '9899965678']
height = len(lines)
width = len(lines[0])
board = [[0 for i in range(width)] for j in range(height)]
for y, line in enumerate(lines):
    for x, char in enumerate(line):
        board[y][x] = int(char)
low_coords = []
# scan for low points - points lower than their adjacent squares
def is_lower_than_adjacent(coord): 
    x, y = coord
    #print(f'x{x} y{y}')
    lowest = board[y][x]
    number = lowest
    scan_coords = []
    if y > 0:
        scan_coords.append((y - 1, x))
    if y < height - 1:
        scan_coords.append((y + 1, x))
    if x > 0:
        scan_coords.append((y, x - 1))
    if x < width - 1:
        scan_coords.append((y, x + 1))
    low_count = 0
    for j, i in scan_coords:    
        if board[j][i] > number:
            low_count += 1
    if low_count == len(scan_coords):
        low_coords.append((x, y))
        return board[y][x] + 1
    else:
        return 0

def find_basin(coord, bi):
    x, y = coord
    if board[y][x] == 9:
        return 0
    if coord not in basins[bi]:
        basins[bi].append(coord)
    scan_coords = []
    if y > 0:
        scan_coords.append((x, y - 1))
    if y < height - 1:
        scan_coords.append((x, y + 1))
    if x > 0:
        scan_coords.append((x - 1, y))
    if x < width - 1:
        scan_coords.append((x + 1, y))
    for xx, yy in scan_coords:
        if (xx, yy) not in basins[bi]:
            #print(f'about to scan {(xx,yy)}')
            #print(f'scan{scan_coords} basin{basins[bi]}')
            #input()
            #basins[bi].append((xx, yy))
            find_basin((xx, yy), bi)
    return 0

sum_lowest = 0      
for y, row in enumerate(board):
    for x, number in enumerate(row):
        #sum_lowest += is_lower_than_adjacent(board, (x, y))
        sum_lowest += is_lower_than_adjacent((x, y))
print(f'part 1: {sum_lowest}')
basins = [[] for j in range(len(low_coords))]
for idx, (x, y) in enumerate(low_coords):
    find_basin((x, y), idx)

sizes = []
product = 1
for idx, basin in enumerate(basins):

    sizes.append(len(basin))
sizes.sort(reverse=True)
for size in sizes[:3]:
    product *= size
print(f'part 2: {product}')
