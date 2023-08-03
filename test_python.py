import pytest

def fibonacci_function(n):
    if n <= 0 :
        raise ValueError('Value must be positive!')
    elif n == 1 : 
        return 0
    elif n == 2 : 
        return 1 
    else :
        return fibonacci_function(n - 1) + fibonacci_function(n - 2)

    
class TestClass : 
    def test_fibonacci_function() :
        assert fibonacci_function(8) == 13
