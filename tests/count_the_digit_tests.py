import codewars_test as test

from katas.count_the_digit import nb_dig


@test.describe("Basic Tests")
def basic_tests():
    @test.it("Basic tests")
    def basic_tests():
        test.assert_equals(nb_dig(5750, 0), 4700)
        test.assert_equals(nb_dig(11011, 2), 9481)
        test.assert_equals(nb_dig(12224, 8), 7733)
        test.assert_equals(nb_dig(11549, 1), 11905)
        test.assert_equals(nb_dig(14550, 7), 8014)
        test.assert_equals(nb_dig(8304, 7), 3927)
        test.assert_equals(nb_dig(10576, 9), 7860)
        test.assert_equals(nb_dig(12526, 1), 13558)
        test.assert_equals(nb_dig(7856, 4), 7132)
        test.assert_equals(nb_dig(14956, 1), 17267)
