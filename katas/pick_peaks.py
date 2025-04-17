# [3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 3]
def pick_peaks(arr):
    if len(arr) == 0:
        return {"pos": [], "peaks": []}

    pos = []
    peaks = []

    for i in range(1, len(arr) - 1):
        if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
            pos.append(i)

    for i in range(1, len(pos)):
        peaks.append(arr[pos])

    return {"pos": pos, "peaks": peaks}