from typing import Any, Tuple

def validate_email(email: str) -> Tuple[bool, str]:
    if "@" in email and "." in email:
        return True, ""
    return False, "Invalid email"

def validate_positive_number(value: Any) -> Tuple[bool, str]:
    if isinstance(value, (int, float)) and value > 0:
        return True, ""
    return False, "Must be positive number"

def validate_customer_input(data: dict):
    if "name" not in data:
        return False, "Missing name"
    return validate_email(data.get("email", ""))

def validate_product_input(data: dict):
    if "name" not in data:
        return False, "Missing name"
    return validate_positive_number(data.get("price"))

def validate_order_input(data: dict):
    if not isinstance(data.get("customer_id"), int):
        return False, "Invalid customer_id"
    if not isinstance(data.get("product_id"), int):
        return False, "Invalid product_id"
    return validate_positive_number(data.get("quantity"))