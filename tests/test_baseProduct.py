import pytest
from src.baseProduct import BaseProduct
from src.product import Product


def test_cannot_instantiate_base_class():
    # Попытка создать экземпляр абстрактного класса должна вызвать TypeError
    with pytest.raises(TypeError):
        BaseProduct()


def test_new_product_inheritance():
    # Проверяем, что наследник реализует метод и возвращает объект нужного типа
    data = {
        'name': 'Книга',
        'description': 'Учебник по программированию',
        'price': 25.5,
        'quantity': 10
    }
    product = Product.new_product(data)
    assert isinstance(product, Product)
