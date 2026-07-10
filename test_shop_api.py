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

# # Run python -m pytest test_shop_api.py -v
# PS C:\Users\GS02494\Desktop\pytest-practice> python -m pytest test_shop_api.py -v
# ======================================================================== test session starts =========================================================================
# platform win32 -- Python 3.14.3, pytest-9.1.1, pluggy-1.6.0 -- C:\Users\GS02494\AppData\Local\Python\pythoncore-3.14-64\python.exe
# cachedir: .pytest_cache
# rootdir: C:\Users\GS02494\Desktop\pytest-practice
# configfile: pytest.ini
# collected 9 items                                                                                                                                                     

# test_shop_api.py::test_status_ok PASSED                                                                                                                         [ 11%]
# test_shop_api.py::test_total_item PASSED                                                                                                                        [ 22%]
# test_shop_api.py::test_first_item_name PASSED                                                                                                                   [ 33%]
# test_shop_api.py::test_first_item_price PASSED                                                                                                                  [ 44%]
# test_shop_api.py::test_second_item_not_in_stock PASSED                                                                                                          [ 55%]
# test_shop_api.py::test_valid_prices[9.99] PASSED                                                                                                                [ 66%]
# test_shop_api.py::test_valid_prices[4.99] PASSED                                                                                                                [ 77%]
# test_shop_api.py::test_valid_prices[1.99] PASSED                                                                                                                [ 88%]
# test_shop_api.py::test_valid_prices[14.99] PASSED                                                                                                               [100%]

# ========================================================================= 9 passed in 0.05s ==========================================================================

# # Run python -m pytest test_shop_api.py -m smoke -v
# PS C:\Users\GS02494\Desktop\pytest-practice> python -m pytest test_shop_api.py -m smoke -v
# ======================================================================== test session starts =========================================================================
# platform win32 -- Python 3.14.3, pytest-9.1.1, pluggy-1.6.0 -- C:\Users\GS02494\AppData\Local\Python\pythoncore-3.14-64\python.exe
# cachedir: .pytest_cache
# rootdir: C:\Users\GS02494\Desktop\pytest-practice
# configfile: pytest.ini
# collected 9 items / 6 deselected / 3 selected                                                                                                                         

# test_shop_api.py::test_status_ok PASSED                                                                                                                         [ 33%]
# test_shop_api.py::test_total_item PASSED                                                                                                                        [ 66%]
# test_shop_api.py::test_first_item_name PASSED                                                                                                                   [100%]

# ================================================================== 3 passed, 6 deselected in 0.04s ===================================================================

# # Push to GitHubgit add, git commit -m, git push
# PS C:\Users\GS02494\Desktop\pytest-practice> git add test_shop_api.py
# PS C:\Users\GS02494\Desktop\pytest-practice> git commit -m "Add Shop API with fixture, marker and parametrize"
# [main 81c4f3d] Add Shop API with fixture, marker and parametrize
#  1 file changed, 54 insertions(+)
#  create mode 100644 test_shop_api.py
# PS C:\Users\GS02494\Desktop\pytest-practice> git push 
# Enumerating objects: 4, done.
# Counting objects: 100% (4/4), done.
# Delta compression using up to 4 threads
# Compressing objects: 100% (3/3), done.
# Writing objects: 100% (3/3), 883 bytes | 294.00 KiB/s, done.
# Total 3 (delta 1), reused 0 (delta 0), pack-reused 0 (from 0)
# remote: Resolving deltas: 100% (1/1), completed with 1 local object.
# To https://github.com/ravindra-QA/pytest-practice.git
#    9aae126..81c4f3d  main -> main