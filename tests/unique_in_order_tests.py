import codewars_test as test

from katas.unique_in_order import unique_in_order


@test.describe("Sample Tests")
def sample_tests():
    @test.it("Should work with empty sequence")
    def _():
        test.assert_equals(unique_in_order(""), [])
        test.assert_equals(unique_in_order([]), [])
        test.assert_equals(unique_in_order(()), [])

    @test.it("Should work with single element sequence")
    def _():
        test.assert_equals(unique_in_order("A"), ["A"])
        test.assert_equals(unique_in_order(["A"]), ["A"])
        test.assert_equals(unique_in_order(("A",)), ["A"])

    @test.it("Should reduce duplicates")
    def _():
        test.assert_equals(unique_in_order("AA"), ["A"])
        test.assert_equals(unique_in_order("AAAABBBCCDAABBB"), ["A", "B", "C", "D", "A", "B"])

    @test.it("Should be case-sensitive")
    def _():
        test.assert_equals(unique_in_order("ABBCcA"), ["A", "B", "C", "c", "A"])

    @test.it("Should work with different element types")
    def _():
        test.assert_equals(unique_in_order([1, 2, 3, 3, -1]), [1, 2, 3, -1])
        test.assert_equals(unique_in_order(["a", "b", "b", "a"]), ["a", "b", "a"])