from .product import Product


class Toys(Product):

    def __init__(self, name: str, model: int,
                 colour: str, price: int,
                 quantity: int):
        """
        Initialize Toys product.
        """
        super().__init__(
            name=name,
            model=model,
            colour=colour,
            price=price,
            quantity=quantity,
            category="Toys"

        )

    def is_returnable(self) -> bool:
        """Return whether the product is returnable."""
        return True  # Toys are always returnable.

    def expiry_date(self) -> str:
        """Return the expiry date of
        the product if applicable."""
        return None
