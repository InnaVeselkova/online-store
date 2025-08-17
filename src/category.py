from typing import List
from src.product import Product


class Category:
    # Атрибуты класса
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: List[Product]):
        self.name = name
        self.description = description
        self.__products = products

        # Обновляем счетчики после добавления всех продуктов
        Category.category_count += 1
        Category.product_count += len(products)

    @property
    def products_(self):
        return self.__products

    def _add_product_internal(self, product: Product):
        """Приватный метод для добавления продукта в список."""
        self.__products.append(product)
        return self.__products

    def add_product(self, product: Product):
        """Публичный метод для добавления продукта."""
        self._add_product_internal(product)
        Category.product_count += 1
        return self.__products

    def __str__(self):
        # Возвращает строку с информацией о продуктах
        total_quantity = sum(product.quantity for product in self.__products)
        return f"Категория: {self.name}. Количество продуктов: {total_quantity} шт."


if __name__ == "__main__":  # pragma: no cover
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(product1.name)
    print(product1.description)
    print(product1.price)
    print(product1.quantity)

    print(product2.name)
    print(product2.description)
    print(product2.price)
    print(product2.quantity)

    print(product3.name)
    print(product3.description)
    print(product3.price)
    print(product3.quantity)

    category1 = Category("Смартфоны",
                         "Смартфоны, как средство коммуникации",
                         [product1, product2, product3])

    print(category1.name == "Смартфоны")
    print(category1.description)
    print(len(category1.products_))
    print(category1.category_count)
    print(category1.product_count)

    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category2 = Category("Телевизоры",
                         "Современный телевизор",
                         [product4])

    print(category2.name)
    print(category2.description)
    print(len(category2.products_))
    print(category2.products_)

    print(Category.category_count)
    print(Category.product_count)
