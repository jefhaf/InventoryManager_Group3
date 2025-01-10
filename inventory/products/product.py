from abc import ABC, abstractmethod
import uuid


class Product(ABC):
    """
    A base class for products.

    arguments:
    id (str): Unique identifier for the product.
    make (str): make of the product.
    model (int): Model number of the product.
    colour (str): Colour of the product.
    price (int): Price of the product.
    quantity (int): Quantity of the product.
    """

    def __init__(
        self,
        make: str,
        model: int,
        colour: str,
        price: float,
        quantity: int,
        category: str,
    ):

        self.id = self.assign_id(category)
        self.make = make
        self.model = model
        self.__price = price
        self.quantity = quantity
        self.colour = colour
        self.category = category

    @abstractmethod
    def is_returnable(self) -> bool:
        """Return whether the product is returnable."""
        pass

    @abstractmethod
    def expiry_date(self) -> str:
        """Return the expiry date of
        the product if applicable."""
        pass

    def assign_id(self, category: str) -> str:
        """Generate a unique ID using the
        category prefix and UUID."""
        prefix = category[:2].upper()
        unique_id = str(uuid.uuid4().int)[:8]
        return f"{prefix}{unique_id}"

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price: float):
        self.__price = new_price

    def update_quantity(self, quantity: int):
        self.quantity += quantity

    def get_total_price(self) -> int:
        """Calculate the total price based on quantity."""
        return self.__price * self.quantity

    def to_dict(self) -> dict:
        """Serialize the product to a dictionary."""
        return {
            "id": self.id,
            "make": self.make,
            "model": self.model,
            "colour": self.colour,
            "price": self.price,
            "quantity": self.quantity,
            "category": self.category,
        }

    @classmethod
    def from_dict(cls, data: dict):
        """
        Deserialize a product from a dictionary.
        """
        instance = cls(
            make=data["make"],
            model=data["model"],
            colour=data["colour"],
            price=data["price"],
            quantity=data["quantity"],
        )

        return instance

    def __str__(self):
        return (
            f"ID: {self.id}, make: {self.make}, Model: {self.model}, "
            f"Colour: {self.colour}, "
            f"Price: {self.__price}, Quantity: {self.quantity}, "
            f"Total Price: {self.get_total_price()}, "
            f"Category: {self.category}"
        )
