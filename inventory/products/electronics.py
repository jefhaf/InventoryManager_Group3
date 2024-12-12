from .product import Product


class Electronics(Product):
    def __init__(
        self,
        name: str,
        model: int,
        colour: str,
        price: float,
        quantity: int,
        warranty_years: int,
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
            category="Electronics"
        )

        self._warranty_years = warranty_years

    def is_returnable(self) -> bool:
        """Return whether the product is returnable."""
        pass

    def expiry_date(self) -> str:
        """Return the expiry date of
        the product if applicable."""
        pass

    def warranty_years(self):
        return self._warranty_years

    def __str__(self):
        base_info = super().__str__()
        return f"{base_info}, Warranty: {self._warranty_years} years"
