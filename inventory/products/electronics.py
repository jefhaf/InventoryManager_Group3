from .product import Product


class Electronics(Product):
    def __init__(
        self,
        make: str,
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
            make=make,
            model=model,
            colour=colour,
            price=price,
            quantity=quantity,
            category="Electronics",
        )

        self.warranty_years = warranty_years

    def is_returnable(self) -> bool:
        """Return whether the product is returnable."""
        return True  # Electronics are always returnable.

    def expiry_date(self) -> str:
        """Return the expiry date of
        the product if applicable."""
        return None

    def warranty_years(self):
        return self.warranty_years

    def __str__(self):
        base_info = super().__str__()
        return f"{base_info}, Warranty: {self.warranty_years} years"

    def to_dict(self) -> dict:
        """Serialize the Electronics product to a dictionary."""
        base_dict = super().to_dict()
        base_dict["warranty_years"] = self.warranty_years
        return base_dict

    @classmethod
    def from_dict(cls, data: dict):
        """Deserialize an Electronics
        product from a dictionary."""

        category = data.get("category", "Electronics")
        if category != "Electronics":
            raise ValueError("Invalid category for Electronics product")

        instance = cls(
            make=data["make"],
            model=data["model"],
            colour=data["colour"],
            price=data["price"],
            quantity=data["quantity"],
            warranty_years=data["warranty_years"],
        )

        instance.category = category

        return instance
