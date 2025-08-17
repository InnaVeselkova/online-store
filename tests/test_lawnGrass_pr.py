import pytest
from src.smartphone_product import Smartphone
from src.lawnGrass_product import LawnGrass


def test_lawngrass_init(sample_lawngrass):
    assert sample_lawngrass.name == "grass"
    assert sample_lawngrass.description == "for lawn"
    assert sample_lawngrass.price == 50.0
    assert sample_lawngrass.quantity == 7
    assert sample_lawngrass.country == "Germany"
    assert sample_lawngrass.germination_period == "sometime"
    assert sample_lawngrass.color == "green"


def test_lawngrass_add():
    grass_sample_1 = LawnGrass("grass", "for lawn", 50.0, 7, "Germany", "sometime", "green")
    # Общая стоимость 350
    grass_sample_2 = LawnGrass("grass", "for lawn", 60.0, 5, "France", "sometime", "red")
    # Общая стоимость 300
    total_cost = grass_sample_1 + grass_sample_2
    assert total_cost == 650


def test_lawngrass_add_error():
    smartphone_1 = Smartphone("Samsung Galaxy C23 Ultra", "Хороший", 100.0, 3, "Высокая", " C23 Ultra", "1 Gb", "red")
    grass_sample = LawnGrass("grass", "for lawn", 50.0, 7, "Germany", "sometime", "green")
    with pytest.raises(TypeError):
        smartphone_1 + grass_sample
