def rot13(message):

    l_alphabet = "abcdefghijklmnopqrstuvwxyz"
    u_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ret = []

    for letter in message:
        pos = l_alphabet. find(letter)
        if pos == -1:
            pos = u_alphabet.find(letter)
            if pos == -1:
                ret += letter
            else:
                np = (pos + 13) % 26
                ret += u_alphabet[np]
        else:
            np = (pos + 13) % 26
            ret += u_alphabet[np]

if __name__ == '__main__':
    rot13('Avoid success at all costs!', 'world')
