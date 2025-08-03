import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def sample_product():
    return Product(
        name="Samsung Galaxy C23 Ultra",
        description="256GB, Серый цвет, 200MP камера",
        price=180000.0,
        quantity=5
    )


@pytest.fixture
def sample_category_products():
    return Category(
        name="Смартфоны",
        description="Смартфоны, как средство коммуникации",
        products=[
            Product(
                name="Samsung Galaxy C23 Ultra",
                description="256GB, Серый цвет, 200MP камера",
                price=180000.0,
                quantity=5
            ),
            Product(
                name="Iphone 15",
                description="512GB, Gray space",
                price=210000.0,
                quantity=8
            ),
            Product(
                name="Xiaomi Redmi Note 11",
                description="1024GB, Синий",
                price=31000.0,
                quantity=14
            )
        ]
    )


@pytest.fixture
def sample_products():
    return [
        Product(name="Product 1", description="Desc 1", price=100.0, quantity=10),
        Product(name="Product 2", description="Desc 2", price=200.0, quantity=20),
        Product(name="Product 3", description="Desc 3", price=300.0, quantity=30),
    ]
