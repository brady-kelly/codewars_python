# Count the Digit Kata
def nb_dig(n, d):

    sq_string = ""
    for i in range(0, n + 1):
        sq_string += str(i ** 2)

    return sq_string.count(str(d))


if __name__ == "__main__":
    nb_dig(11549, 1)