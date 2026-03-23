import requests
import pytest

BASE_URL = "http://localhost:8080/api/v1"

VALID_HEADERS = {
    "X-Roll-Number": "2024115007",
    "X-User-ID": "1"
}

# ----------------------------
# HEADER TESTS (6)
# ----------------------------

def test_missing_roll_number():
    r = requests.get(f"{BASE_URL}/profile", headers={"X-User-ID": "1"})
    assert r.status_code == 401

def test_missing_user_id():
    r = requests.get(f"{BASE_URL}/profile", headers={"X-Roll-Number": "2024115007"})
    assert r.status_code == 401

def test_both_headers_missing():
    r = requests.get(f"{BASE_URL}/profile")
    assert r.status_code == 401

def test_invalid_user_id_string():
    headers = {"X-Roll-Number": "2024115007", "X-User-ID": "abc"}
    r = requests.get(f"{BASE_URL}/profile", headers=headers)
    assert r.status_code == 400

def test_negative_user_id():
    headers = {"X-Roll-Number": "2024115007", "X-User-ID": "-1"}
    r = requests.get(f"{BASE_URL}/profile", headers=headers)
    assert r.status_code in [400, 401]

def test_large_user_id():
    headers = {"X-Roll-Number": "2024115007", "X-User-ID": "999999"}
    r = requests.get(f"{BASE_URL}/profile", headers=headers)
    assert r.status_code in [200, 400]


# ----------------------------
# PROFILE TESTS (3)
# ----------------------------

def test_valid_profile():
    r = requests.get(f"{BASE_URL}/profile", headers=VALID_HEADERS)
    assert r.status_code == 200

def test_profile_wrong_method():
    r = requests.post(f"{BASE_URL}/profile", headers=VALID_HEADERS)
    assert r.status_code in [400, 405]

def test_profile_empty_headers():
    r = requests.get(f"{BASE_URL}/profile", headers={})
    assert r.status_code == 401


# ----------------------------
# ADDRESS TESTS (6)
# ----------------------------

def test_valid_address():
    data = {"label": "HOME", "street": "Street A", "city": "CityX", "pincode": "500001"}
    r = requests.post(f"{BASE_URL}/addresses", headers=VALID_HEADERS, json=data)
    assert r.status_code in [200, 201]

def test_invalid_address_short_fields():
    data = {"label": "H", "street": "A", "city": "X", "pincode": "123"}
    r = requests.post(f"{BASE_URL}/addresses", headers=VALID_HEADERS, json=data)
    assert r.status_code == 400

def test_missing_address_field():
    data = {"label": "HOME", "city": "CityX"}
    r = requests.post(f"{BASE_URL}/addresses", headers=VALID_HEADERS, json=data)
    assert r.status_code == 400

def test_invalid_pincode_alpha():
    data = {"label": "HOME", "street": "Street", "city": "City", "pincode": "ABCDE"}
    r = requests.post(f"{BASE_URL}/addresses", headers=VALID_HEADERS, json=data)
    assert r.status_code == 400

def test_empty_address():
    r = requests.post(f"{BASE_URL}/addresses", headers=VALID_HEADERS, json={})
    assert r.status_code == 400

def test_long_address_values():
    data = {"label": "HOME"*50, "street": "Street"*50, "city": "City"*50, "pincode": "500001"}
    r = requests.post(f"{BASE_URL}/addresses", headers=VALID_HEADERS, json=data)
    assert r.status_code in [200, 400]


# ----------------------------
# CART TESTS (10)
# ----------------------------

def test_valid_cart_add():
    data = {"product_id": 1, "quantity": 1}
    r = requests.post(f"{BASE_URL}/cart/add", headers=VALID_HEADERS, json=data)
    assert r.status_code in [200, 201]

def test_negative_quantity():
    data = {"product_id": 1, "quantity": -1}
    r = requests.post(f"{BASE_URL}/cart/add", headers=VALID_HEADERS, json=data)
    assert r.status_code == 400

def test_zero_quantity():
    data = {"product_id": 1, "quantity": 0}
    r = requests.post(f"{BASE_URL}/cart/add", headers=VALID_HEADERS, json=data)
    assert r.status_code == 400

def test_large_quantity():
    data = {"product_id": 1, "quantity": 100000}
    r = requests.post(f"{BASE_URL}/cart/add", headers=VALID_HEADERS, json=data)
    assert r.status_code in [200, 400]

def test_missing_product_id():
    data = {"quantity": 1}
    r = requests.post(f"{BASE_URL}/cart/add", headers=VALID_HEADERS, json=data)
    assert r.status_code == 400

def test_invalid_product_id_type():
    data = {"product_id": "abc", "quantity": 1}
    r = requests.post(f"{BASE_URL}/cart/add", headers=VALID_HEADERS, json=data)
    assert r.status_code == 400

def test_float_quantity():
    data = {"product_id": 1, "quantity": 2.5}
    r = requests.post(f"{BASE_URL}/cart/add", headers=VALID_HEADERS, json=data)
    assert r.status_code in [400, 200]

def test_string_quantity():
    data = {"product_id": 1, "quantity": "two"}
    r = requests.post(f"{BASE_URL}/cart/add", headers=VALID_HEADERS, json=data)
    assert r.status_code == 400

def test_empty_cart_request():
    r = requests.post(f"{BASE_URL}/cart/add", headers=VALID_HEADERS, json={})
    assert r.status_code == 400

def test_bulk_add():
    data = {"product_id": 1, "quantity": 9999}
    r = requests.post(f"{BASE_URL}/cart/add", headers=VALID_HEADERS, json=data)
    assert r.status_code in [200, 400]


# ----------------------------
# EDGE / ROBUSTNESS TESTS (5)
# ----------------------------

def test_invalid_endpoint():
    r = requests.get(f"{BASE_URL}/invalid", headers=VALID_HEADERS)
    assert r.status_code == 404

def test_wrong_method_cart():
    r = requests.get(f"{BASE_URL}/cart/add", headers=VALID_HEADERS)
    assert r.status_code in [400, 405]

def test_no_json_body():
    r = requests.post(f"{BASE_URL}/cart/add", headers=VALID_HEADERS)
    assert r.status_code == 400

def test_extra_fields():
    data = {"product_id": 1, "quantity": 1, "extra": "test"}
    r = requests.post(f"{BASE_URL}/cart/add", headers=VALID_HEADERS, json=data)
    assert r.status_code in [200, 400]

def test_repeated_requests():
    data = {"product_id": 1, "quantity": 1}
    for _ in range(5):
        r = requests.post(f"{BASE_URL}/cart/add", headers=VALID_HEADERS, json=data)
        assert r.status_code in [200, 400]