import re

def pick_peaks(arr):
    pos = []
    peaks = []
    plats = []

    plat_pat = re.compile("(\d)\1+")
    arr_str = ''.join([chr(x) for x in arr])
    repeats = plat_pat.finditer(arr_str)

    for r in repeats:
        place = r.span()
        num = r.group()[0]
        if place[0] > 0 and place[1] < len(arr) - 1 and arr[place[0] - 1] < num and arr[place[1] + 1] < num:
            plats.append(place)

    start = 0
    for p in plats:
        pos.append(p[0])



    return {"pos": pos, "peaks": peaks}

if __name__ == '__main__':
    pick_peaks([2,1,3,1,2,2,2,2,1])

