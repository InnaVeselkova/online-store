import json
import os
from typing import List, Dict


class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


def load_product_json(path: str) -> List[Dict]:
    full_path = os.path.abspath(path)
    with open(full_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        return data


if __name__ == '__main__':  # pragma: no cover
    print(load_product_json("../data/products.json"))
