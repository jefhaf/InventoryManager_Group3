from .product import Product


class Food(Product):

    def __init__(
        self,
        make: str,
        model: int,
        colour: str,
        price: float,
        expiration_date: str,
        quantity: int,
    ):
        """
        Initialize Food product with expiration_date.
        """
        super().__init__(make,
                         model, colour,
                         price, quantity,
                         category="Food")

        self.expiration_date = expiration_date

    def is_returnable(self) -> bool:
        """Return whether the product is returnable."""
        return False  # Foods are not returnable.

    def expiry_date(self) -> str:
        """Return the expiry date of
        the product if applicable."""
        return self.expiration_date

    def __str__(self):
        base_info = super().__str__()
        return f"{base_info}, Expiration Date: {self.expiration_date}"
