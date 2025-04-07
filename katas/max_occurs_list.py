def delete_nth(order,max_e):
    num_counts = {}
    ret = []

    for item in order:
        nc = num_counts.get(item, 0)
        if nc < max_e:
            ret.append(item)
            num_counts[item] = nc + 1
    return ret

if __name__ == "__main__":
    delete_nth([20, 37, 20, 21], 1)