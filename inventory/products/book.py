from .product import Product


class Book(Product):
    def __init__(
        self,
        make: str,
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
            make=make,
            model=model,
            colour=colour,
            price=price,
            quantity=quantity,
            category="Book",
        )

        self.author = author

    def is_returnable(self) -> bool:
        """Return whether the product is returnable."""
        return True  # Books are always returnable.

    def expiry_date(self) -> str:
        """Return the expiry date of
        the product if applicable."""
        return None

    def __str__(self):
        base_info = super().__str__()
        return f"{base_info}, Author: {self.author}"

    def to_dict(self) -> dict:
        """Serialize the Electronics product to a dictionary."""
        base_dict = super().to_dict()
        base_dict["author"] = self.author
        return base_dict

    @classmethod
    def from_dict(cls, data: dict):
        """Deserialize an Book
        product from a dictionary."""

        category = data.get("category", "Book")
        if category != "Book":
            raise ValueError("Invalid category for Book product")

        instance = cls(
            make=data["make"],
            model=data["model"],
            colour=data["colour"],
            price=data["price"],
            quantity=data["quantity"],
            author=data["author"],
        )

        instance.category = category

        return instance
