from framework import _routes
import views

def dispatch(request: dict) -> dict:
    key = (request.get("method"), request.get("path"))
    view = _routes.get(key)

    if not view:
        return {"status_code": 404, "body": "Not Found", "headers": {}}

    return view(request)

# fake_request = {
#     "method": "POST",
#     "path": "/products",
#     "session": {"user_id": 1, "role": "admin"}, 
#     "body": {"name": "IPhone 15", "price": 1200},
#     "query": {}
# }

# response = dispatch(fake_request)

# print("СТАТУС:", response["status_code"])
# print("ВІДПОВІДЬ:", response["body"])