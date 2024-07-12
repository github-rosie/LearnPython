# tests/test_pytest_mock.py 
import pytest
from LearnPython.mock_examples.calculator import calculate
from LearnPython.mock_examples.area import area_of_circle


################# Mock Constants or Variables #################

def test_area_of_circle(mocker):
    mocker.patch('LearnPython.mock_examples.area.PI', 3.0)
    assert area_of_circle(5) == 75.0


################# Mock Functions #################

def test_calculate_add(mocker):
    # Mock the add function in the calculator module
    # The mocker.patch method is used to replace the add function with a mock that returns 5.
    mock_add = mocker.patch('LearnPython.mock_examples.calculator.add', return_value=5)
    # Call the calculate function with 'add' operation
    result = calculate('add', 2, 3)
    ####### Verify that the mock_add function was called with the correct arguments #######
    mock_add.asset_called_once_with(2, 3)
    # Verify that the result is as expected
    assert result == 5

def test_calculate_subtract(mocker):
    mock_subtract = mocker.patch('LearnPython.mock_examples.calculator.subtract', return_value=-4)
    result = calculate('subtract', 5, 9)
    mock_subtract.assert_called_once_with(5, 9)
    assert result == -4


