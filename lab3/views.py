from framework import app
from middleware import audit_log, login_required, role_required
from models import *
from validators import *
from templates import *

@app.get("/customers")
@audit_log
@login_required
def get_customers(request):
    return {
        "status_code": 200,
        "body": render_json(get_all_customers()),
        "headers": {"Content-Type": "application/json"}
    }

@app.post("/customers")
@audit_log
@role_required("admin")
def create_customer_view(request):
    valid, error = validate_customer_input(request["body"])
    if not valid:
        return {"status_code": 400, "body": render_error(error), "headers": {}}

    data = create_customer(request["body"])
    return {"status_code": 201, "body": render_json(data), "headers": {}}

@app.get("/products")
@audit_log
def get_products(request):
    return {
        "status_code": 200,
        "body": render_json(get_all_products()),
        "headers": {}
    }

@app.post("/products")
@audit_log
@role_required("admin")
def create_product_view(request):
    valid, error = validate_product_input(request["body"])
    if not valid:
        return {"status_code": 400, "body": render_error(error), "headers": {}}

    data = create_product(request["body"])
    return {"status_code": 201, "body": render_json(data), "headers": {}}

@app.post("/orders")
@audit_log
@login_required
def create_order_view(request):
    valid, error = validate_order_input(request["body"])
    if not valid:
        return {"status_code": 400, "body": render_error(error), "headers": {}}

    order = create_order(request["body"])
    if not order:
        return {"status_code": 400, "body": render_error("Invalid IDs"), "headers": {}}

    return {"status_code": 201, "body": render_json(order), "headers": {}}

@app.get("/orders")
@audit_log
@role_required("admin")
def get_orders(request):
    return {
        "status_code": 200,
        "body": render_json(get_all_orders()),
        "headers": {}
    }