from .product import Product


class Apparel(Product):

    def __init__(self, make: str, model: int,
                 colour: str, price: int, quantity: int):
        """
        Initialize Apparel product.
        """
        super().__init__(
            make=make,
            model=model,
            colour=colour,
            price=price,
            quantity=quantity,
            category="Apparel",
        )

    def is_returnable(self) -> bool:
        """Return whether the product is returnable."""
        return True

    def expiry_date(self) -> str:
        """Return the expiry date of
        the product if applicable."""
        return None
