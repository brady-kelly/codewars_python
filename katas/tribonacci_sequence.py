# Tribonacci Sequence kata
def tribonacci(signature, n):
    trib = signature[0:min(n, 3)]
    i = 0
    while len(trib) < n:
        trib_sum = sum(trib[i:i + 3])
        i += 1
        trib.append(trib_sum)
    return trib

if __name__ == "__main__":
    tribonacci([300, 200, 100], 2)