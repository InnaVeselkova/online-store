import json
import os
from typing import Dict, List


class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, data: Dict) -> 'Product':
        return cls(
            name=data.get('name'),
            description=data.get('description'),
            price=float(data.get('price')),
            quantity=int(data.get('quantity'))
        )

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, value: float):
        if value <= 0:
            print("Цена не должна быть нулевой или отрицательной")
        else:
            self.__price = value


def load_product_json(path: str) -> List[Dict]:
    full_path = os.path.abspath(path)
    with open(full_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        return data


if __name__ == '__main__':  # pragma: no cover
    print(load_product_json("../data/products.json"))
