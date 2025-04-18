import re

def pick_peaks(arr):
    pos = []
    plats = []

    plat_pat = re.compile(r"(\d)\1+")
    arr_str = ''.join([str(x) for x in arr])
    repeats = plat_pat.finditer(arr_str)

    for r in repeats:
        place = r.span()
        num = int(r.group()[0])
        if place[0] > 0 and place[1] - 1 < len(arr):
            before = arr[place[0]-1]
            after = arr[place[1]-1]
            if before < num and after < num:
                plats.append((place[0], place[1] -1))

    if len(plats) > 0:
        start = 1
        for p in plats:
            pos.append(p[0])
            for i in range(start, p[0] - 1):
                if arr[i - 1] < arr[i] and arr[i + 1] < arr[i]:
                    start = p[1] + 1
                    pos.append(i)
    else:
        # [21312222]
        # {01234567]
        for i in range(1, len(arr)):
            if arr[i - 1] < arr[i] and arr[i + 1] < arr[i]:
                pos.append(i)

    pos.sort()
    peaks = [arr[i] for i in pos]

    return {"pos": pos, "peaks": peaks}

if __name__ == '__main__':
    pick_peaks([3,2,3,6,4,1,2,3,2,1,2,2,2,1])

