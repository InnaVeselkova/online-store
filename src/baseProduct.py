from abc import ABC, abstractmethod


class BaseProduct(ABC):

    @classmethod
    @abstractmethod
    def new_product(cls, data):
        """Создает новый продукт из словаря данных."""
        pass
