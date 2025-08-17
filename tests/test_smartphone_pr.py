import pytest
from src.smartphone_product import Smartphone
from src.lawnGrass_product import LawnGrass


def test_smartphone_init(sample_smartphone):
    assert sample_smartphone.name == "Samsung Galaxy C23 Ultra"
    assert sample_smartphone.description == "Хороший"
    assert sample_smartphone.price == 100.0
    assert sample_smartphone.quantity == 3
    assert sample_smartphone.efficiency == "Высокая"
    assert sample_smartphone.model == " C23 Ultra"
    assert sample_smartphone.memory == "1 Gb"
    assert sample_smartphone.color == "red"


def test_smartphone_add():
    smartphone_1 = Smartphone("Samsung Galaxy C23 Ultra", "Хороший", 100.0, 3, "Высокая", " C23 Ultra", "1 Gb", "red")
    # Общая стоимость 300
    smartphone_2 = Smartphone("Samsung Galaxy C2", "Нормальный", 10.0, 2, "Нормальная", " C2", "5 Gb", "grey")
    # Общая стоимость 20
    total_cost = smartphone_1 + smartphone_2
    assert total_cost == 320


def test_smartphone_add_error():
    smartphone_1 = Smartphone("Samsung Galaxy C23 Ultra", "Хороший", 100.0, 3, "Высокая", " C23 Ultra", "1 Gb", "red")
    grass_sample = LawnGrass("grass", "for lawn", 50.0, 7, "Germany", "sometime", "green")
    with pytest.raises(TypeError):
        smartphone_1 + grass_sample
