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
            raise ValueError('Товара недостаточно на складе')

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
         - Если quantity не передан, то удаляется вся позиция
         - Если quantity меньше, чем количество продуктов в позиции - уменьшаем количество продуктов
         в позиции на переданную величину quantity.
         - Если quantity больше, чем количество продуктов в позиции, то удаляется вся позиция
        """
        if product in self.products \
                and (quantity is None or quantity >= self.products[product]):
            del self.products[product]
        else:
            self.products[product] -= quantity

    def clear(self):
        self.products.clear()

    def get_total_price(self) -> float:
        total_price = 0.00
        for product in self.products:
            total_price += self.products[product] * product.price
        return round(total_price, 2)

    def buy(self):
        """
        Метод покупки.
        Учтите, что товаров может не хватать на складе.
        В этом случае нужно выбросить исключение ValueError
        """
        for product in self.products:
            product.buy(self.products[product])
            # try:
            #     product.buy(self.products[product])
            # except ValueError:
            #     raise ValueError('Товара недостаточно на складе')
        return self.get_total_price()

if __name__ == "__main__":
    product = Product("book", 100, "This is a book", 1000)
    product.buy(10)
    cart = Cart()
    cart.add_product(product)
    print(cart.get_total_price())