"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


@pytest.fixture
def cart():
    cart = Cart()
    return cart


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # напишите проверки на метод check_quantity

        """
        Тест на проверку того, что метод check_quantity возвращает True при передаче значения quantity,
        которое меньше или равно quantity объекта Product, и False в обратном случае.
        """
        assert product.check_quantity(product.quantity - 1) is True
        assert product.check_quantity(product.quantity) is True
        assert product.check_quantity(product.quantity + 1) is False

    def test_product_buy(self, product):
        # напишите проверки на метод buy
        """
        Тест на проверку того, что метод buy уменьшает количество товара на складе на переданное значение quantity
         в случае, если это количество товара есть на складе,
        """
        product.buy(product.quantity - 1)
        assert product.quantity == 1

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError):
            product.buy(product.quantity + 1)


class TestCart:
    """
    Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_add_product_to_cart_with_default_quantity_1_when_product_is_not_in_cart(self, cart, product):
        cart.add_product(product)
        assert product in cart.products
        assert cart.products[product] == 1

    def test_add_product_to_cart_with_default_quantity_1_when_product_is_already_in_cart(self, cart, product):
        cart.add_product(product)
        cart.add_product(product)
        assert product in cart.products
        assert cart.products[product] == 2

    def test_add_product_to_cart_with_specified_quantity_when_product_is_not_in_cart(self, cart, product):
        cart.add_product(product, product.quantity)
        assert product in cart.products
        assert cart.products[product] == product.quantity

    def test_add_product_to_cart_with_specified_quantity_when_product_is_already_in_cart(self, cart, product):
        cart.add_product(product)
        cart.add_product(product, product.quantity - 1)
        assert product in cart.products
        assert cart.products[product] == product.quantity

    def test_remove_product_from_cart_with_quantity_0(self, cart, product):
        cart.add_product(product)
        cart.remove_product(product)
        assert cart.products == {}

    def test_remove_product_from_cart_with_quantity_greater_than_available_product_quantity(self, cart, product):
        cart.add_product(product)
        cart.remove_product(product, product.quantity + 1)
        assert cart.products == {}

    def test_remove_product_from_cart_with_quantity_less_than_cart_product_quantity(self, cart, product):
        cart.add_product(product, product.quantity)
        cart.remove_product(product, cart.products[product] - 1)
        assert cart.products[product] == 1

    def test_remove_product_from_cart_with_quantity_equal_cart_product_quantity(self, cart, product):
        cart.add_product(product, product.quantity)
        cart.remove_product(product, cart.products[product])
        assert cart.products.get(product) is None

    def test_clear_cart_not_empty(self, cart, product):
        cart.add_product(product)
        cart.clear()
        assert cart.products == {}

    def test_clear_cart_is_empty(self, cart, product):
        cart.clear()
        assert cart.products == {}

    def test_get_total_price_with_single_product_in_cart(self, cart, product):
        cart.add_product(product, product.quantity)
        assert cart.get_total_price() == product.price * product.quantity

    def test_buy_with_enough_quantity_is_successful(self, cart, product):
        cart.add_product(product, product.quantity - 1)
        # assert cart.buy() == product.price * 999
        cart.buy()
        assert product.quantity == 1

    def test_buy_when_not_enough_quantity_raises_value_error_(self, cart, product):
        cart.add_product(product, product.quantity + 1)
        with pytest.raises(ValueError) as exc_info:
            cart.buy()
        assert str(exc_info.value) == 'Товара недостаточно на складе'
        assert exc_info.type == ValueError
