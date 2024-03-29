from series.series import fibonacci, lucas, sum_series


def test_fibonacci_zero():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected

def test_fibonacci_one():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected

def test_fibonacci_two():
    actual = fibonacci(2)
    expected = 1
    assert actual == expected

def test_fibonacci_ten():
    actual = fibonacci(10)
    expected = 55
    assert actual == expected


def test_lucas_zero():
    actual = lucas(0)
    expected = 2
    assert actual == expected

def test_lucas_one():
    actual = lucas(1)
    expected = 1
    assert actual == expected

def test_lucas_two():
    actual = lucas(2)
    expected = 3
    assert actual == expected

def test_lucas_three():
    actual = lucas(3)
    expected = 4
    assert actual == expected

def test_lucas_ten():
    actual = lucas(10)
    expected = 123
    assert actual == expected


def test_sum_series_fib_ten():
    actual = sum_series(10)
    expected = 55
    assert actual == expected

def test_sum_series_lucas_ten():
    actual = sum_series(10,2,1)
    expected = 123
    assert actual == expected