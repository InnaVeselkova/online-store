# Интернет-магазин

## Описание проекта

Данный проект ...

## Установка

Для установки проекта:
1. Клонируйте репозиторий: 
git clone https://github.com/InnaVeselkova/online-store
2. Активируйте виртуальное окружение:
python -m venv venv
source venv/bin/activate   # для Linux/MacOS
venv\Scripts\activate    # для Windows
3. Установите необходимые зависимости:
pip install -r requirements.txt

## Использование

### 1. Классы Category и Product

Классы Category и Product находятся в отдельных файлах модуля src. Они сохраняют общую информацию. 
Класс Product содержит следующие свойства: название (name), описание (description), цену (price), 
количество в наличии (quantity). Для класса Category свойства: название (name), описание (description), 
список товаров категории (products), а также реализовано два атрибута класса: количество категорий и количество товаров.
