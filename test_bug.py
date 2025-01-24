# pytest; pip instal pytest

from new_func import a, b, add_two_numbers, subtract_two_numbers, multiply_two_numbers
import numpy as np
#print(a, b, add_two_numbers(a, b), subtract_two_numbers(a, b), multiply_two_numbers(a, b))

def test_a_functionality():

	a, b = 10, 20

	assert add_two_numbers(a, b) == 30 # What assert does is that it checks if the condition is true, if it is true, it does nothing, if it is false, it raises an AssertionError

#By corollary, we should not name any of actual code files with names starting with "test"

def test_b_functionality():

	a, b = np.random.randint(1, 100, 2)

	assert subtract_two_numbers(a, b) == a - b, "Subtraction failed"
	assert multiply_two_numbers(a, b) == a * b, "Multiplication failed"

def test_b_functionalityy():

	a, b = 10, 20

	assert subtract_two_numbers(a, b) == -10, "Subtraction failed"
	assert multiply_two_numbers(a, b) == 200