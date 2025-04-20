import codewars_test as test

from katas.roman_numerals_helper import RomanNumerals


@test.describe('fixed tests')
def fixed_tests():

    def do_test(input, expected):
        func = RomanNumerals.to_roman if type(input) is int else RomanNumerals.from_roman
        actual = func(input)
        test.assert_equals(actual, expected, f'testing {func.__name__}, for input {input}\n')

    @test.it('to roman')
    def fixed_tests_to():
        do_test(1000, 'M')
        do_test(4, 'IV')
        do_test(1, 'I')
        do_test(1990, 'MCMXC')
        do_test(2008, 'MMVIII')

    @test.it('from roman')
    def fixed_tests_from():
        do_test('XXI', 21)
        do_test('I', 1)
        do_test('IV', 4)
        do_test('MMVIII', 2008)
        do_test('MDCLXVI', 1666)