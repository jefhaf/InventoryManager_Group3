from product import Product


class Electronics(Product):
    def __init__(
        self,
        id: str,
        name: str,
        model: int,
        colour: str,
        price: float,
        warranty_years: int,
        quantity: int = 1,
    ):
        """
        Initialize Electronics product with warranty_years.
        """
        super().__init__(id, name, model, colour, price, quantity)
        self._warranty_years = warranty_years

    def category(self):
        return "Electronics"

    @property
    def warranty_years(self):
        return self._warranty_years

    def get_product_info(self):
        base_info = super().get_product_info()
        return f"{base_info}, Warranty: {self._warranty_years} years"
