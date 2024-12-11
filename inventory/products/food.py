from product import Product


class Food(Product):

    def __init__(
        self,
        id: str,
        name: str,
        model: int,
        colour: str,
        price: float,
        expiration_date: str,
        quantity: int = 1,
    ):
        """
        Initialize Food product with expiration_date.
        """
        super().__init__(id, name, model, colour, price, quantity)
        self._expiration_date = expiration_date

    def category(self):
        return "Food"

    def get_product_info(self):
        base_info = super().get_product_info()
        return f"{base_info}, Expiration Date: {self._expiration_date}"
