import pytest
from src.category import Category
from src.product import Product


def test_category_products_init(sample_category_products):
    assert sample_category_products.name == "Смартфоны"
    assert sample_category_products.description == "Смартфоны, как средство коммуникации"
    assert len(sample_category_products.products_) == 3


def test_multiple_categories_increase_counts():
    # Обнуляем счетчики перед тестом
    Category.category_count = 0
    Category.product_count = 0

    Category("Fruits", "Fresh fruits", [Product("Apple", 5, 10, 9)])
    Category("Vegetables", "Fresh vegetables", [Product("Carrot", 3, 15, 6)])

    assert Category.category_count == 2
    assert Category.product_count == 2


def test_category_initialization(sample_products):
    # Создаем категорию
    category = Category(
        name="Electronics",
        description="Electronic gadgets",
        products=sample_products
    )

    # Проверяем атрибуты объекта
    assert category.name == "Electronics"
    assert category.description == "Electronic gadgets"
    # Проверка списка продуктов
    assert category.products_ == sample_products


def test_create_category_with_products(sample_products_2):
    # Проверка счетчиков
    initial_category_count = Category.category_count
    initial_product_count = Category.product_count

    category = Category("Фрукты", "Описание", sample_products_2)

    # Проверка атрибутов
    assert category.name == "Фрукты"
    assert category.description == "Описание"
    # Проверка внутреннего списка продуктов
    assert len(category.products_) == len(sample_products_2)

    # Проверка счетчиков
    assert Category.category_count == initial_category_count + 1
    assert Category.product_count == initial_product_count + len(sample_products_2)


def test_internal_products_list_is_private():
    # Проверка приватности
    p1 = Product("Книга X", "Описание X", 120.0, 4)
    category = Category("Тестовая категория", "Описание", [p1])

    with pytest.raises(AttributeError):
        _ = category.__products


def test_products_info_returns_correct_string():
    # Создаем продукты с учетом количества
    p1 = Product("Книга А", "Описание А", 50.0, 1)
    p2 = Product("Книга Б", "Описание Б", 75.5, 2)
    category = Category("Категория", "Описание", [p1, p2])

    info_str = category.products

    # Проверяем, что строка содержит информацию о каждом продукте в новом формате
    assert f"{p1.name}, {p1.price} руб. Остаток: {p1.quantity} шт." in info_str
    assert f"{p2.name}, {p2.price} руб. Остаток: {p2.quantity} шт." in info_str

    # Проверяем, что строки разделены переносом и правильные
    lines = info_str.split("\n")
    assert len(lines) == 2
    assert lines[0] == f"{p1.name}, {p1.price} руб. Остаток: {p1.quantity} шт."
    assert lines[1] == f"{p2.name}, {p2.price} руб. Остаток: {p2.quantity} шт."
