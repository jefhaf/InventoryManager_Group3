import pytest
from inventory.products import product
from inventory.products.book import Book
from inventory.products.household import Household
from inventory.products.electronics import Electronics
from inventory.products.apparel import Apparel
from inventory.products.food import Food
from inventory.products.toys import Toys


@pytest.fixture
def sample_book():
    book1 = Book(
        make="Houghton Mifflin",
        model="Lord of the Rings",
        colour="Red",
        price=22.99,
        author="Tolkien",
        quantity=1,
    )
    return book1


@pytest.fixture
def sample_household():
    household1 = Household(
        make="Vorwerk",
        model="Thermomix TM6",
        colour="White",
        price=799.99,
        quantity=1,
    )
    return household1


@pytest.fixture
def sample_electronics():
    electronics1 = Electronics(
        make="Samsung",
        model="Galaxxy S23",
        colour="White",
        price=699.99,
        quantity=1,
        warranty_years=2,
    )
    return electronics1


@pytest.fixture
def sample_food():
    food1 = Food(
        make="Gorilla Foods",
        model="Superfood for bunkers",
        colour="grey",
        price=20.00,
        quantity=1,
        expiration_date="01.01.2050 12:00:00",
    )
    return food1


@pytest.fixture
def sample_apparel():
    apparel1 = Apparel(
        make="Clothing Company",
        model="Hackerhoody",
        colour="black",
        price=25.00,
        quantity=1,
    )
    return apparel1


@pytest.fixture
def sample_toys():
    toys1 = Toys(
        make="Lego",
        model="Deathstar",
        colour="black",
        price=499.99,
        quantity=1,
    )
    return toys1


# region Individual
class TestIndividualStuff:

    def test_to_dict(self, sample_book):
        sample_book.id = "BO123"
        result_dict = sample_book.to_dict()
        test_dict = {
            "id": "BO123",
            "make": "Houghton Mifflin",
            "category": "Book",
            "model": "Lord of the Rings",
            "colour": "Red",
            "price": 22.99,
            "quantity": 1,
            "author": "Tolkien",
        }
        assert result_dict == test_dict

    def test_str_method_book(self, sample_book):

        expected_total_price = sample_book.price * sample_book.quantity
        expected_str = (
            f"ID: {sample_book.id}, "
            f"make: {sample_book.make}, "
            f"Model: {sample_book.model}, "
            f"Colour: {sample_book.colour}, "
            f"Price: {sample_book.price}, "
            f"Quantity: {sample_book.quantity}, "
            f"Total Price: {expected_total_price}, "
            f"Category: {sample_book.category}, "
            f"Author: {sample_book.author}"
        )
        assert str(sample_book) == expected_str

    def test_str_method_electronics(self, sample_electronics):

        expected_total_price = sample_electronics.price * sample_electronics.quantity
        expected_str = (
            f"ID: {sample_electronics.id}, "
            f"make: {sample_electronics.make}, "
            f"Model: {sample_electronics.model}, "
            f"Colour: {sample_electronics.colour}, "
            f"Price: {sample_electronics.price}, "
            f"Quantity: {sample_electronics.quantity}, "
            f"Total Price: {expected_total_price}, "
            f"Category: {sample_electronics.category}, "
            f"Warranty: {sample_electronics.warranty_years} years"
        )
        assert str(sample_electronics) == expected_str

    def test_str_method_food(self, sample_food):

        expected_total_price = sample_food.price * sample_food.quantity
        expected_str = (
            f"ID: {sample_food.id}, "
            f"make: {sample_food.make}, "
            f"Model: {sample_food.model}, "
            f"Colour: {sample_food.colour}, "
            f"Price: {sample_food.price}, "
            f"Quantity: {sample_food.quantity}, "
            f"Total Price: {expected_total_price}, "
            f"Category: {sample_food.category}, "
            f"Expiration Date: {sample_food.expiration_date}"
        )
        assert str(sample_food) == expected_str

# endregion


class TestAddition2:

    @pytest.mark.parametrize(
        "sample_product",
        [
            "sample_book",
            "sample_household",
            "sample_electronics",
            "sample_food",
            "sample_apparel",
            "sample_toys",
        ],
    )
    def test_quantity(self, sample_product, request):
        sample_product = request.getfixturevalue(sample_product)
        print(type(sample_product))
        old_quantity = sample_product.quantity
        sample_product.update_quantity(5)
        new_quantity = sample_product.quantity
        assert new_quantity == old_quantity + 5

    @pytest.mark.parametrize(
        "sample_product",
        [
            "sample_book",
            "sample_household",
            "sample_electronics",
            "sample_food",
            "sample_apparel",
            "sample_toys",
        ],
    )
    def test_price(self, sample_product, request):
        sample_product = request.getfixturevalue(sample_product)
        price = sample_product.price
        assert isinstance(price, float)
        assert price > 0

        # Test the setter and getter
        new_price = 10.99
        sample_product.price = new_price
        assert sample_product.price == new_price

    @pytest.mark.parametrize(
        "sample_product, expected_category",
        [
            ("sample_book", "Book"),
            ("sample_household", "Household"),
            ("sample_electronics", "Electronics"),
            ("sample_food", "Food"),
            ("sample_apparel", "Apparel"),
            ("sample_toys", "Toys"),
        ],
    )
    def test_correct_category(self,
                              sample_product,
                              expected_category,
                              request):
        sample_product = request.getfixturevalue(sample_product)
        assert sample_product.category == expected_category


    @pytest.mark.parametrize(
        "sample_product",
        [
            "sample_household",
            "sample_apparel",
            "sample_toys",
        ],
    )
    def test_str_method(self, sample_product, request):
        sample_product = request.getfixturevalue(sample_product)
        expected_total_price = sample_product.price * sample_product.quantity
        expected_str = (
            f"ID: {sample_product.id}, "
            f"make: {sample_product.make}, "
            f"Model: {sample_product.model}, "
            f"Colour: {sample_product.colour}, "
            f"Price: {sample_product.price}, "
            f"Quantity: {sample_product.quantity}, "
            f"Total Price: {expected_total_price}, "
            f"Category: {sample_product.category}"
        )
        assert str(sample_product) == expected_str

    @pytest.mark.parametrize(
        "sample_product, expected_returnable",
        [
            ("sample_book", True),
            ("sample_household", True),
            ("sample_electronics", True),
            ("sample_food", False),
            ("sample_apparel", True),
            ("sample_toys", True),
        ],
    )
    def test_returnable(self, sample_product, expected_returnable, request):
        sample_product = request.getfixturevalue(sample_product)
        returnable = sample_product.is_returnable()
        assert returnable == expected_returnable
