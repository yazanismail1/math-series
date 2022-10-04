import pytest 
from math_series.series import lucas_series, fibonacci_series, sum_series

def test_fibonacci_series_one():
    assert fibonacci_series(0) == 0
    assert fibonacci_series(1) == 1
    assert fibonacci_series(2) == 1
    assert fibonacci_series(10) == 55
    assert fibonacci_series(-1) == "Please enter a positive integer"
    assert fibonacci_series("hi") == "Please enter a positive integer"

def test_lucas_series_one():
    assert lucas_series(0) == 2
    assert lucas_series(1) == 1
    assert lucas_series(2) == 3
    assert lucas_series(10) == 123
    assert lucas_series(-1) == "Please enter a positive integer"
    assert lucas_series("hi") == "Please enter a positive integer"

def test_sum_series_one():
    assert sum_series(0) == 0
    assert sum_series(1) == 1
    assert sum_series(2) == 1
    assert sum_series(10) == 55
    assert sum_series(-1) == "Please enter a positive integer"
    assert sum_series("hi") == "Please enter a positive integer"
    assert sum_series(0,first_num=0,second_num=1) == 0
    assert sum_series(1,first_num=0,second_num=1) == 1
    assert sum_series(2,first_num=0,second_num=1) == 1
    assert sum_series(10,first_num=0,second_num=1) == 55
    assert sum_series(-1,first_num=0,second_num=1) == "Please enter a positive integer"
    assert sum_series("hi",first_num=0,second_num=1) == "Please enter a positive integer"
    assert sum_series(0,first_num=2,second_num=1) == 2
    assert sum_series(1,first_num=2,second_num=1) == 1
    assert sum_series(2,first_num=2,second_num=1) == 3
    assert sum_series(10,first_num=2,second_num=1) == 123
    assert sum_series(-1,first_num=2,second_num=1) == "Please enter a positive integer"
    assert sum_series("hi",first_num=2,second_num=1) == "Please enter a positive integer"
    assert sum_series(0,first_num=5,second_num=8) == 5
    assert sum_series(1,first_num=5,second_num=8) == 8
    assert sum_series(2,first_num=5,second_num=8) == 13
    assert sum_series(10,first_num=5,second_num=8) == 610
    assert sum_series(-1,first_num=5,second_num=8) == "Please enter a positive integer"
    assert sum_series("hi",first_num=5,second_num=8) == "Please enter a positive integer"
    assert sum_series(0,first_num=-3,second_num=-5) == -3
    assert sum_series(1,first_num=-3,second_num=-5) == -5
    assert sum_series(2,first_num=-3,second_num=-5) == -8
    assert sum_series(10,first_num=-3,second_num=-5) == -377
    assert sum_series(-1,first_num=-3,second_num=-5) == "Please enter a positive integer"
    assert sum_series("hi",first_num=-3,second_num=-5) == "Please enter a positive integer"
