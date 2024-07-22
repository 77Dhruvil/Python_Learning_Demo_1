import pytest
import allure

@allure.title("TC#1 2-2=0 verify")
@allure.description("This test case verifies the substraction of 2-2=0")
@pytest.mark.smoke
def test_substraction():
    assert 2 - 2 == 0

@allure.title("TC#2 3-3=0 verify")
@allure.description("This test case verifies the substraction of 3-3=0")
@pytest.mark.sannity
def test_substraction1():
    assert 3 - 3 == 0

@allure.title("TC#3 4-4=0 verify")
@allure.description("This test case verifies the substraction of 4-4=0")
@pytest.mark.regression
def test_substraction2():
    assert 4 - 4 == 0

@allure.title("TC#4 4-3=0 verify")
@allure.description("This test case verifies the substraction of 4-3=0")
@pytest.mark.smoke
def test_substraction3():
    assert 4 - 4 != 0