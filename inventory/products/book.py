from .product import Product


class Book(Product):
    def __init__(
        self,
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
        super().__init__(
            name=name,
            model=model,
            colour=colour,
            price=price,
            quantity=quantity,
            category="Book"
        )

        self.author = author

    def is_returnable(self) -> bool:
        """Return whether the product is returnable."""
        pass

    def expiry_date(self) -> str:
        """Return the expiry date of
        the product if applicable."""
        pass

    def __str__(self):
        base_info = super().__str__()
        return f"{base_info}, Author: {self._author}"
