import pytest

from inventory.products import product
from inventory.products.book import Book


@pytest.fixture
def sample_book():
    book1 = Book(
        name="Lord of the Rings",
        model=1,
        colour="Red",
        price=22.99,
        author="Tolkien",
        quantity=1,
    )
    return book1


class TestBook:

    def test_correct_category(self, sample_book):
        assert sample_book.category == "Book"

    def test_price(self, sample_book):
        price = sample_book.price
        assert isinstance(price, float)
        assert price > 0

        # Test the setter and getter
        new_price = 10.99
        sample_book.price = new_price
        assert sample_book.price == new_price

    def test_quantity(self, sample_book):
        old_quantity = sample_book.quantity
        sample_book.update_quantity(5)
        new_quantity = sample_book.quantity
        assert new_quantity == old_quantity + 5

    def test_to_dict(self, sample_book):
        sample_book.id = "BO123"
        result_dict = sample_book.to_dict()
        test_dict = {
            "id": "BO123",
            "category": "Book",
            "name": "Lord of the Rings",
            "model": 1,
            "colour": "Red",
            "price": 22.99,
            "quantity": 1,
        }
        assert result_dict == test_dict


# Not yet implemented

# def test_str_method(self, sample_book):

#     expected_total_price = sample_book.price * sample_book.quantity
#     expected_str = (
#         f"Product(ID: {sample_book.id}, Name: {sample_book.name}, Model: {sample_book.model}, "
#         f"Colour: {sample_book.colour}, "
#         f"Price: {sample_book.price}, Quantity: {sample_book.quantity}, "
#         f"Total Price: {expected_total_price})"
#     )
#     assert str(sample_book) == expected_str


# def test_sold_out(self, sample_book):

#     if sample_book.quantity > 0:
#         assert sample_book.is_sold_out()

#     elif sample_book.quantity == 0:
#         assert not sample_book.is_sold_out()


# def test_returnable(self, sample_book):
#         returnable = sample_book.is_returnable()
#         assert isinstance(returnable, bool)


# def test_is_returnable(self, sample_book):
#     returnable = sample_book.is_returnable()
#     assert isinstance(returnable, bool)
