def unique_in_order(sequence):
    ret = []

    for i in range(0, len(sequence)):
        if len(ret) == 0 or sequence[i] != ret[-1]:
            ret.append(sequence[i])

    return ret