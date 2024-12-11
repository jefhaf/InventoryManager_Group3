from product import Product


class Book(Product):
    def __init__(
        self,
        id: str,
        name: str,
        model: int,
        colour: str,
        price: float,
        author: str,
        quantity: int = 1,
    ):
        """
        Initialize Electronics product with warranty_years.
        """
        super().__init__(id, name, model, colour, price, quantity)
        self.author = author

    def category(self):
        return "Book"

    def __str__(self):
        base_info = super().get_product_info()
        return f"{base_info}, Author: {self._author}"
