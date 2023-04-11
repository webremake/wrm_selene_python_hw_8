class Product:
    """
    Класс продукта
    """
    name: str
    price: float
    description: str
    quantity: int

    def __init__(self, name, price, description, quantity):
        self.name = name
        self.price = price
        self.description = description
        self.quantity = quantity

    def check_quantity(self, quantity) -> bool:
        """
        Возвращаем True если количество продукта больше или равно запрашиваемому
        и False в обратном случае
        """
        return self.quantity >= quantity

    def buy(self, quantity):
        """
        Проверяем количество продукта используя метод check_quantity
        Если продуктов не хватает, то исключение ValueError
        """
        if self.check_quantity(quantity) is True:
            self.quantity -= quantity
        else:
            raise ValueError \
                (f'Товара {self.name} недостаточно на складе. Не хватает {self.quantity - quantity} шт.')

    def __hash__(self):
        return hash(self.name + self.description)


class Cart:
    """
    Класс корзины. В нем хранятся продукты, которые пользователь хочет купить.
    TODO реализуйте все методы класса
    """

    # Словарь продуктов и их количество в корзине
    products: dict[Product, int]

    def __init__(self):
        # По-умолчанию корзина пустая
        self.products = {}

    def add_product(self, product: Product, quantity=1):
        """
        Метод добавления продукта в корзину.
        Если продукт уже есть в корзине, то увеличиваем количество
        """
        if product in self.products:
            self.products[product] += quantity
        else:
            self.products[product] = quantity


    def remove_product(self, product: Product, quantity=None):
        """
        Метод удаления продукта из корзины.
        Если quantity не передан, то удаляется вся позиция
        Если quantity больше, чем количество продуктов в позиции, то удаляется вся позиция
        """
        raise NotImplementedError

    def clear(self):
        raise NotImplementedError

    def get_total_price(self) -> float:
        raise NotImplementedError

    def buy(self):
        """
        Метод покупки.
        Учтите, что товаров может не хватать на складе.
        В этом случае нужно выбросить исключение ValueError
        """
        raise NotImplementedError


if __name__ == "__main__":
    book = Product("book", 100, "This is a book", 1000)
    newspaper = Product("newspaper", 20, "This is a newspaper", 5000)
    jornal = Product("jornal", 50, "This is a jornal", 2000)
    cart = Cart()
    cart.add_product(book, 5)
    print(cart.products)
    cart.add_product(book, 5)
    print(cart.products)
    cart.add_product(newspaper, 10)
    print(cart.products)
    cart.add_product(newspaper, 5)
    print(cart.products)




    # book.buy(100)


    print()

