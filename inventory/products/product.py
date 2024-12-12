from abc import ABC, abstractmethod


class Product(ABC):
    """
    A base class for products.

    arguments:
    id (str): Unique identifier for the product.
    name (str): Name of the product.
    model (int): Model number of the product.
    colour (str): Colour of the product.
    price (int): Price of the product.
    quantity (int): Quantity of the product.
    """

    def __init__(
        self,
        id: str,
        name: str,
        model: int,
        colour: str,
        price: float,
        quantity: int,
    ):

        self.id = id
        self.name = name
        self.model = model
        self.__price = price
        self.quantity = quantity
        self.colour = colour

    @abstractmethod
    def category(self):
        """Return the category of the product."""
        pass

    @abstractmethod
    def is_returnable(self) -> bool:
        """Return whether the product is returnable."""
        pass

    @abstractmethod
    def warranty_info(self) -> str:
        """Return warranty information
        specific to the product."""
        pass

    @abstractmethod
    def expiry_date(self) -> str:
        """Return the expiry date of
        the product if applicable."""
        pass

    def is_sold_out(self) -> bool:
        """Return whether the product is sold out."""
        return self.quantity == 0

    def assign_id(self) -> str:
        """Generate a unique ID using the
        category prefix and UUID."""
        pass

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price: float):
        self.__price = new_price

    def update_quantity(self, quantity: int):
        self._quantity += quantity

    def get_total_price(self) -> int:
        """Calculate the total price based on quantity."""
        return self.__price * self.quantity

    def __str__(self):
        return (
            f"Product(ID: {self.id}, Name: {self.name}, Model: {self.model}, "
            f"Colour: {self.colour}, "
            f"Price: {self.price}, Quantity: {self.quantity}, "
            f"Total Price: {self.get_total_price()})"
        )
