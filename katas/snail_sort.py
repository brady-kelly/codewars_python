import math

def snail(snail_map):
    size = int(math.sqrt(len(snail_map)))

    ret = []

    col = 0
    row = 0

    while col < size:
        ret.append(snail_map[row][col])
        col += 1

