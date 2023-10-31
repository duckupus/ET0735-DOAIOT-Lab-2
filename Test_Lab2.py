import unittest
import Lab2

def test_find_min_max():
    result = []
    input_data = [1, 4, 6, 3, -2]
    result = Lab2.find_min_max(input_data)
    assert (result[0] == -2)
    assert (result[1] == 6)

def test_calc_average():
    result = 0
    input_data = [2, 2, 2, 4, 4, 4]
    result = Lab2.calc_average(input_data)
    assert (result == 3)

def test_calc_median_temperature():
    repeat = 0
    input_data = [1, 2, 3, 4, 5]
    result = Lab2.calc_median_temperature(input_data)
    assert (result == 3)


if __name__ == '__main__':
    unittest.main()
