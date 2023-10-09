class Product:
    def __init__(self, name: str, price: float, weight: float, country: str):
        self._name = name
        self._price = price
        self._weight = weight
        self._country = country

    @property
    def get_name(self):
        return self._name

    @property
    def get_price(self):
        return self._price

    @property
    def get_weight(self):
        return self._weight

    @property
    def get_country(self):
        return self._country

    def get_product(self):
        return {'name': self.get_name, 'price': self.get_price, 'weight': self.get_weight, 'country': self.get_country}


class ProductPlace:
    def __init__(self, product, quantity):
        self._product_name = product.get_name()
        self._product = product
        self._quantity = quantity

    @property
    def get_product_name(self):
        return self._product_name

    @property
    def get_product(self):
        return self._product

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        if value >= self._quantity:
            self._quantity -= value
        else:
            print("Don't have so many products")

    def add_quantity(self, value: int):
        self._quantity += value

    def remove_quantity(self, value: int):
        self.quantity -= value

    def get_place_product(self):
        return {'name': self.get_product_name, 'quantity': self.quantity}


class Store:
    def __init__(self):
        self._products = {}

    def add_new_product(self, item: ProductPlace):
        self._products.update({item.get_product_name: item})

    def add_quantity(self, name: str, quantity: int):
        self._products[name]
