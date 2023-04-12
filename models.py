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
        if product in self.products \
                and (quantity is None or quantity > self.products[product]):
            del self.products[product]

    def clear(self):
        self.products.clear()

    def get_total_price(self) -> float:
        total_price = 0.00
        for product in self.products:
            total_price += self.products[product] * product.price
        return total_price

    def buy(self):
        """
        Метод покупки.
        Учтите, что товаров может не хватать на складе.
        В этом случае нужно выбросить исключение ValueError
        """

        # для каждого товара в корзине применяем метод Product.buy
        # если ни для одного товара метод не выбросил исключение возвращаем True и очишаем корзину
        for product in self.products:
            try:
                product.buy(self.products[product])
            except:
                print(f'Товара {product.name} недостаточно на складе.\n'
                      f'Остаток товара на складе {product.quantity} шт.\n'
                      f'Вы можете удалить товар из корзины командой remove_product({product.name}),\n'
                      f'Или изменить количество товара в корзине change_product_quantity({product.quantity})'
                      )
        return self.get_total_price()
    


if __name__ == "__main__":
    book = Product("book", 99.99, "This is a book", 1000)
    newspaper = Product("newspaper", 19.95, "This is a newspaper", 5000)
    jornal = Product("jornal", 49.81, "This is a jornal", 2000)
    cart = Cart()
    cart.add_product(book, 5)
    cart.add_product(book, 5)
    cart.add_product(newspaper, 10)
    cart.add_product(newspaper, 5000)
    # cart.remove_product(book)
    # cart.remove_product(newspaper, 550)
    cart.get_total_price()
    print(cart.get_total_price())
    cart.buy()
    cart.remove_product(newspaper)


    # cart.clear()

    # book.buy(100)

    print()

    cart.buy()
    cart.get_total_price()
    print(cart.get_total_price())
