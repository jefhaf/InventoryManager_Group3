from .product import Product


class Book(Product):
    def __init__(
        self,
        id: str,
        name: str,
        model: int,
        colour: str,
        price: float,
        author: str,
        quantity: int,
    ):
        """
        Initialize Electronics product with warranty_years.
        """
        super().__init__(id, name, model, colour, price, quantity)
        self.author = author
        self.category = "Book"

    def category(self):
        return "Book"

    def is_returnable(self) -> bool:
        """Return whether the product is returnable."""
        pass

    def warranty_info(self) -> str:
        """Return warranty information
        specific to the product."""
        pass

    def expiry_date(self) -> str:
        """Return the expiry date of
        the product if applicable."""
        pass

    def __str__(self):
        base_info = super().get_product_info()
        return f"{base_info}, Author: {self._author}"
