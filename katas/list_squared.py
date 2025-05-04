import math

def list_squared(m, n):
    ret = []
    for n in range(m, n+1):
        divs = find_divisors(n)
        sqs = sum([n ** 2 for n in divs])
        if is_square(sqs):
            ret.append([n, sqs])
    return ret

def is_square(n):
    if math.ceil(math.sqrt(n)) == math.floor(math.sqrt(n)):
        return True
    else:
        return False

def find_divisors(n):
    divisors = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    divisors.sort()
    return divisors


if __name__ == '__main__':
    list_squared(1, 250)