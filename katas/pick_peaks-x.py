def pick_peaks(arr):
    if len(arr) == 0:
        return {"pos": [], "peaks": []}

    pos = []
    peaks = []
    plat = []

    #[0,1,2,3,4,5,6,7]
    #[2,1,3,2,2,2,2,1]

    for i in range(1, len(arr) - 1):
        cur = arr[i]
        prv = arr[i - 1]
        nxt = arr[i + 1]
        if cur > prv and cur > nxt:
            pos.append(i)
            plat = []
        elif cur == prv and cur == nxt:
            plat.append(i - 1)
        if len(plat) >= 1 and nxt < arr[plat[0]] and arr[plat[0]] > arr[plat[-1]]:
            pos.append(plat[0])
            plat = []

    for i in range(0, len(pos)):
        peaks.append(arr[pos[i]])

    return {"pos": pos, "peaks": peaks}

if __name__ == '__main__':
    pick_peaks([2,1,3,2,2,2,2,1])