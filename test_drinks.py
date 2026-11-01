import pytest
from drinks import Drink, Coffee, Matcha, MENU, create_drink


def test_small_drink_price():
    drink = Drink("Latte", 5.50, "Small")
    assert drink.calculate_price() == 5.50

def test_medium_drink_price():
    drink = Drink("Latte", 5.50, "Medium")
    assert drink.calculate_price() == 5.75

def test_large_drink_price():
    drink = Drink("Latte", 5.50, "Large")
    assert drink.calculate_price() == 6.00

def test_create_coffee():
    drink = create_drink("Iced Vanilla Latte", "Small", "Whole", "Iced")
    assert isinstance(drink, Coffee)

def test_create_matcha():
    drink = create_drink("Matcha Latte", "Small", "Oat", "Hot")
    assert isinstance(drink, Matcha)

def test_invalid_drink():
    with pytest.raises(ValueError):
        create_drink("Invalid Drink", "Small", "Whole", "Hot")