import pytest

def test_string_is_uppercase():
    assert "automation".upper() == "AUTOMATION"

def test_list_length():
    browser_list = ["Chrome", "Firefox", "Safari"]
    assert len(browser_list) == 3

def test_status_code_valid():
    valid_code = [200, 201, 204]
    assert 200 in valid_code

##########################Fixtures##################################

@pytest.fixture
def api_response():
    return {
    "status": 200,
    "message": "Login Successful",
    "user": {
        "id": 101,
        "username": "Allison"
    }
}
    
def test_status_is_200(api_response):
    assert api_response["status"] == 200

def test_message(api_response):
    assert api_response["message"] == "Login Successful"

def test_username(api_response):
    assert api_response["user"]["username"] == "Allison"

###########################Parametrize#################################

@pytest.mark.parametrize("endpoint", ["/login", "/shop", "/logout", "/profile", "/news"])
def test_valid_endpoints(endpoint):
    assert endpoint.startswith("/")

############################Markers################################

@pytest.mark.smoke
def test_home_page():
    assert True

@pytest.mark.regression
def test_full_regression():
    assert len("Allison") > 3


# import pytest

# # ==========================================
# # Task 1 — Basic Tests
# # ==========================================

# def test_string_is_uppercase():
#     assert "automation".upper() == "AUTOMATION"

# def test_list_length():
#     browser_list = ["Chrome", "Firefox", "Safari"]
#     assert len(browser_list) == 3

# def test_status_code_valid():
#     valid_codes = [200, 201, 204]
#     assert 200 in valid_codes


# # ==========================================
# # Task 2 — Fixture
# # ==========================================

# @pytest.fixture
# def api_response():
#     """Provides a mock API response dictionary for testing."""
#     return {
#         "status": 200,
#         "message": "Login Successful",
#         "user": {
#             "id": 101,
#             "username": "Allison"
#         }
#     }

# def test_status_is_200(api_response):
#     assert api_response["status"] == 200

# def test_message(api_response):
#     assert api_response["message"] == "Login Successful"

# def test_username(api_response):
#     assert api_response["user"]["username"] == "Allison"


# # ==========================================
# # Task 3 — Parametrize
# # ==========================================

# @pytest.mark.parametrize("endpoint", [
#     "/login", 
#     "/shop", 
#     "/logout", 
#     "/profile", 
#     "/news"
# ])
# def test_valid_endpoints(endpoint):
#     assert endpoint.startswith("/")


# # ==========================================
# # Task 4 — Markers
# # ==========================================

# @pytest.mark.smoke
# def test_home_page():
#     assert True

# @pytest.mark.regression
# def test_full_regression():
#     assert len("Allison") > 3