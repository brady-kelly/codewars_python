import codewars_test as test

from katas.scramblies import scramble


def dotest(s1, s2, expected):
    actual = scramble(s1, s2)
    test.assert_equals(actual, expected, f"With\ns1 = \"{s1}\"\ns2 = \"{s2}\"")


@test.describe("Tests")
def test_group():
    @test.it("Sample tests")
    def test_case():
        for s1, s2, expected in [
            ('rkqodlw', 'world', True),
            ('cedewaraaossoqqyt', 'codewars', True),
            ('katas', 'steak', False),
            ('scriptjava', 'javascript', True),
            ('scriptingjava', 'javascript', True)
        ]:
            dotest(s1, s2, expected)

    @test.it("Example large test")
    def large_test():
        s1 = "abcdefghijklmnopqrstuvwxyz" * 10_000
        s2 = "zyxcba" * 9_000
        dotest(s1, s2, True)