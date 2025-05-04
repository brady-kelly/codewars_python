import codewars_test as test
from codewars_test import it

from katas.codewars_ranking import User


@it("[-8]")
def _():
    user = User()
    user.inc_progress(-8)
    test.assert_equals(user.rank, -8)
    test.assert_equals(user.progress, 3)

@test.it("[-7]")
def _():
    user = User()
    user.inc_progress(-7)
    test.assert_equals(user.rank, -8)
    test.assert_equals(user.progress, 10)

@test.it("[-6]")
def _():
    user = User()
    user.inc_progress(-6)
    test.assert_equals(user.rank, -8)
    test.assert_equals(user.progress, 40)

@test.it("[-5]")
def _():
    user = User()
    user.inc_progress(-5)
    test.assert_equals(user.rank, -8)
    test.assert_equals(user.progress, 90)

@test.it("[-4]")
def _():
    user = User()
    user.inc_progress(-4)
    test.assert_equals(user.rank, -7)
    test.assert_equals(user.progress, 60)

@test.it("[1, 1]")
def _():
    user = User()
    user.inc_progress(1)
    test.assert_equals(user.rank, -2)
    test.assert_equals(user.progress, 40)
    user.inc_progress(1)
    test.assert_equals(user.rank, -2)
    test.assert_equals(user.progress, 80)