from .product import Product


class Food(Product):

    def __init__(
        self,
        name: str,
        model: int,
        colour: str,
        price: float,
        expiration_date: str,
        quantity: int,
    ):
        """
        Initialize Food product with expiration_date.
        """
        super().__init__(name,
                         model, colour,
                         price, quantity,
                         category="Food")

        self._expiration_date = expiration_date

    def is_returnable(self) -> bool:
        """Return whether the product is returnable."""
        pass

    def expiry_date(self) -> str:
        """Return the expiry date of
        the product if applicable."""
        pass

    def __str__(self):
        base_info = super().__str__()
        return f"{base_info}, Expiration Date: {self._expiration_date}"
