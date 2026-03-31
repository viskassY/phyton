db = {
    "customers": [],
    "products": [],
    "orders": []
}

def get_all_customers():
    return db["customers"]

def create_customer(data):
    data["id"] = len(db["customers"]) + 1
    db["customers"].append(data)
    return data

def get_all_products():
    return db["products"]

def create_product(data):
    data["id"] = len(db["products"]) + 1
    db["products"].append(data)
    return data

def get_all_orders():
    return db["orders"]

def create_order(data):
    customer = next((c for c in db["customers"] if c["id"] == data["customer_id"]), None)
    product = next((p for p in db["products"] if p["id"] == data["product_id"]), None)

    if not customer or not product:
        return None

    total = product["price"] * data["quantity"]

    order = {
        "id": len(db["orders"]) + 1,
        "customer_id": data["customer_id"],
        "product_id": data["product_id"],
        "quantity": data["quantity"],
        "total": total
    }

    db["orders"].append(order)
    return order