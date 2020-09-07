
"""
Auto-testing for lab 06
"""

import pytest
from Lab06 import number_of_special_numbers

def test_n_10000():
    student = number_of_special_numbers(10000)
    assert student == 3

def test_n_100000():
    student = number_of_special_numbers(100000)
    assert student == 39

def test_n_1000000():
    student = number_of_special_numbers(1000000)
    assert student == 396
