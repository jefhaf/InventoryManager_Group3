import pytest
from inventory_manager.inventory_manager import (
    InventoryManager,
    LowPriceException,
)
from inventory_manager.inventory_manager import (
    product_factory,
    check_valid_date_input,
)


@pytest.fixture
def sample_inventory_manager():
    inventory_manager1 = InventoryManager(filename="products_test.json")
    return inventory_manager1


# TODO Parametrize different inputs where we expect to find an existing product
def test_search_product_by_user(sample_inventory_manager, monkeypatch):
    # sample_inventory_manager.search_product_by_user()
    expected_search_result = [
        {
            "id": "EL22694396",
            "make": "jellobeangun",
            "model": "Slinky",
            "colour": "unicorn",
            "price": 420.69,
            "quantity": 7,
            "category": "Electronics",
        }
    ]
    # make, model, low_price, high_price, category, colour
    inputs = iter(["jello", "", "420", "", "electronics", ""])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    result = sample_inventory_manager.search_product_by_user()

    assert isinstance(result, list)
    assert result == expected_search_result


def test_search_product_by_user_3(sample_inventory_manager, monkeypatch):
    # sample_inventory_manager.search_product_by_user()
    expected_search_result = [
        {
            "id": "EL16863242",
            "make": "wrrrggg",
            "model": "wrgwrg",
            "colour": "red",
            "price": 123.0,
            "quantity": 123,
            "category": "Electronics",
            "warranty_years": "222",
        },
        {
            "id": "EL22694396",
            "make": "jellobeangun",
            "model": "Slinky",
            "colour": "unicorn",
            "price": 420.69,
            "quantity": 7,
            "category": "Electronics",
        },
    ]
    # make, model, low_price, high_price, category, colour
    inputs = iter(["", "", "", "", "electronics", ""])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    result = sample_inventory_manager.search_product_by_user()
    print(result)

    assert isinstance(result, list)
    assert result == expected_search_result


def test_search_product_by_user_2(sample_inventory_manager, monkeypatch):
    # sample_inventory_manager.search_product_by_user()
    expected_search_result = {
        "id": "EL22694396",
        "make": "jellobeangun",
        "model": "Slinky",
        "colour": "unicorn",
        "price": 420.69,
        "quantity": 7,
        "category": "Electronics",
    }
    # make, model, low_price, high_price, category, colour
    inputs = iter(["jello", "", "421", "", "electronics", ""])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    result = sample_inventory_manager.search_product_by_user()

    assert not result
    # assert result[0] == None


def test_search_product_by_user_4(sample_inventory_manager, monkeypatch):
    # sample_inventory_manager.search_product_by_user()
    expected_search_result = [
        {
            "id": "EL22694396",
            "make": "jellobeangun",
            "model": "Slinky",
            "colour": "unicorn",
            "price": 420.69,
            "quantity": 7,
            "category": "Electronics",
        }
    ]
    # make, model, low_price, high_price, category, colour
    inputs = iter(["jello", "", "inconvertible", "", "electronics", ""])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    result = sample_inventory_manager.search_product_by_user()

    assert isinstance(result, list)
    assert result == expected_search_result


# def test_search_product_by_user_wrong_category(sample_inventory_manager, monkeypatch):
#     # sample_inventory_manager.search_product_by_user()
#     expected_search_result = {'id': 'TO22694396',
#                               'make': 'jellobeangun',
#                               'model': 'Slinky',
#                               'colour': 'unicorn',
#                               'price': 420.69,
#                               'quantity': 7,
#                               'category': 'Toyssgfasrgrg'}
#     inputs = iter(["jello", "", "", "", "", "", "n"])
#     monkeypatch.setattr('builtins.input', lambda _: next(inputs))
#     result = sample_inventory_manager.search_product_by_user()
#     print(result)

#     assert isinstance(result, list)
#     assert result[0] == None


# TODO Test search function where we expect "not found"


# def test_ask_user_info(monkeypatch):
#     # Mock multiple inputs by using a list and a lambda
#     inputs = iter(["Alice", "30"])
#     monkeypatch.setattr("builtins.input", lambda _: next(inputs))

#     result = ask_user_info()

#     assert result == "Hello, Alice! You are 30 years old."


# Sample Product which exists
# "id": "TO22694396",
#                 "make": "jellobeangun",
#                 "model": "Slinky",
#                 "colour": "unicorn",
#                 "price": 420.69,
#                 "quantity": 7,
#                 "category": "Toys"
