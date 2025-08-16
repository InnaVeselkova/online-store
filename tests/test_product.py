import pytest
from src.product import Product


def test_product_init(sample_product):
    assert sample_product.name == "Samsung Galaxy C23 Ultra"
    assert sample_product.description == "256GB, Серый цвет, 200MP камера"
    assert sample_product.price == 180000.0
    assert sample_product.quantity == 5


def test_initial_price():
    product = Product("Книга", "Учебник", 10.0, 5)
    assert product.price == 10.0


def test_set_valid_price():
    product = Product("Книга", "Учебник", 10.0, 5)
    product.price = 20
    assert product.price == 20


def test_set_zero_price(capsys):
    product = Product("Книга", "Учебник", 10.0, 5)
    product.price = 0
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевой или отрицательной" in captured.out
    # Цена не должна измениться
    assert product.price == 10.0


def test_from_dict_valid_data():
    data = {
        'name': 'Книга',
        'description': 'Учебник по программированию',
        'price': 25.5,
        'quantity': 10
    }
    product = Product.new_product(data)
    assert isinstance(product, Product)
    assert product.name == 'Книга'
    assert product.description == 'Учебник по программированию'
    assert product.price == 25.5
    assert product.quantity == 10


def test_from_dict_invalid_price_and_quantity():
    data = {
        'name': 'Книга',
        'description': 'Учебник',
        'price': 'not_a_number',
        'quantity': 'not_a_number'
    }
    with pytest.raises(ValueError):
        Product.new_product(data)


def test_product_addition():
    # Создаем два продукта
    product1 = Product("Товар 1", "Описание 1", 100, 10)  # Общая стоимость 1000
    product2 = Product("Товар 2", "Описание 2", 200, 2)   # Общая стоимость: 400

    # Складываем продукты
    total_cost = product1 + product2
    assert total_cost == 1400


def test_product_str():
    product1 = Product("Товар 1", "Описание 1", 100, 10)

    result = str(product1)
    assert result == "Товар 1, 100.0 руб. Остаток: 10 шт."
