# Create test_shop_api.py

# Add import pytest
import pytest

# Write fixture shop_response returning this dictionary: {"status": 200, "items": [{"name": "Skin", "price": 9.99, "in_stock": True}, {"name": "Bundle", "price": 4.99, "in_stock": False}], "total_items": 2}
@pytest.fixture
def shop_response():
    return {
        "status": 200,
        "items": [
            {
                "name": "Skin",
                "price": 9.99,
                "in_stock": True
            },
            {
                "name": "Bundle",
                "price": 4.99, 
                "in_stock": False
            }
        ],
        "total_items": 2
    }

# test_status_ok — checks status is 200 Mark as smoke
@pytest.mark.smoke
def test_status_ok(shop_response):
    assert shop_response["status"] == 200

# test_total_items — checks total_items equals 2Mark as smoke
@pytest.mark.smoke
def test_total_item(shop_response):
    assert len(shop_response["items"]) == 2

# test_first_item_name — checks first item name is "Skin"     items[0]["name"]
@pytest.mark.smoke
def test_first_item_name(shop_response):
    assert shop_response["items"][0]["name"] == "Skin"

# test_first_item_price — checks first item price is 9.99     Mark as regression
@pytest.mark.regression
def test_first_item_price(shop_response):
    assert shop_response["items"][0]["price"] == 9.99

# test_second_item_not_in_stock — checks second item in_stock is False      Mark as regression
@pytest.mark.regression
def test_second_item_not_in_stock(shop_response):
    assert shop_response["items"][1]["in_stock"] == False

# Write parametrized test test_valid_prices checking these prices are all greater than 0: [9.99, 4.99, 1.99, 14.99]@pytest.mark.parametrize
@pytest.mark.parametrize("prices", [9.99, 4.99, 1.99, 14.99])
def test_valid_prices(prices):
    assert prices > 0