from src.category import Category
from src.product import Product


def test_category_products_init(sample_category_products):
    assert sample_category_products.name == "Смартфоны"
    assert sample_category_products.description == "Смартфоны, как средство коммуникации"
    Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    assert len(sample_category_products.products) == 3


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
    assert category.products == sample_products


def test_empty_products_list():
    # Тестирование категории без продуктов
    category = Category("EmptyCategory", "No products here", [])

    assert category.products == []
