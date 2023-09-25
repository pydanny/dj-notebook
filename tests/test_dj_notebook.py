from dj_notebook import activate


def test_thing():
    plus = activate("test_harness")
    # TODO capture STDOUT and assert on it
    assert plus.print() is None
