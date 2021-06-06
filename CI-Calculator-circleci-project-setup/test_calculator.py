"""
Tests for calc app
"""
import calculator


class TestCalculatorApp:
    def test_add(self):
        assert 5 == calculator.add(3,2)
    
    def test_subtract(self):
        assert 5 == calculator.subtract(10, 5)
    
    def test_multiply(self):
      assert 4 == calculator.multiply(2, 2)
    
    def test_divide(self):
      assert 2 == calculator.divide(4, 2)
