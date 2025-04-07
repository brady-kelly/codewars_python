import collections

def scramble(s1, s2):
    s1_count = collections.Counter(s1)
    s2_count = collections.Counter(s2)

    for n2 in s2_count.keys():
        if n2 not in s1_count or s1_count[n2] < s2_count[n2]:
            return False
    return True

if __name__ == '__main__':
    scramble('rkqxdlw', 'world')

