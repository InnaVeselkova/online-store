from src.product import Product


def test_repr_output():
    # Создаем объект продукта
    product = Product("Товар", "Описание", 1000.0, 5)

    # Формируем ожидаемый результат
    expected_repr = "Product (Товар, Описание, 1000.0, 5)"

    # Проверяем, что __repr__ возвращает ожидаемую строку
    assert repr(product) == expected_repr
