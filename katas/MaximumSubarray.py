def max_sequence(arr):
    neg = sum(1 for i in arr if i < 0)
    if neg == len(arr):
        return 0
    else:
        pos = sum(1 for i in arr if i > 0)
        if pos == len(arr):
            return sum(arr)
        else:
            max_seq = []
            max_tot = 0
            for start in range(0, len(arr)):
                for end in range(start, len(arr)):
                    seq = arr[start: end]
                    tot = sum(seq)
                    if tot > max_tot:
                        max_seq = seq
                        max_tot = tot
            return sum(max_seq)


if __name__ == "__main__":
    max_sequence([7, 4, 11, -11, 39, 36, 10, -6, 37, -10, -32, 44, -26, -34, 43, 43])
