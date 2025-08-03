def test_product_init(sample_product):
    assert sample_product.name == "Samsung Galaxy C23 Ultra"
    assert sample_product.description == "256GB, Серый цвет, 200MP камера"
    assert sample_product.price == 180000.0
    assert sample_product.quantity == 5
