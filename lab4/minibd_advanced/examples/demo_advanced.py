from minidb.database import Database
from minidb.core.column import Column
from minidb.core.datatypes import IntegerType
from minidb.query.engine import Count, Query

# створення бази
db = Database("test_db")

# створення таблиці
users = db.create_table("users", [
    Column("id", IntegerType(), unique=True)
])

# вставка даних
users.insert({"id": 1}, database=db)
users.insert({"id": 2}, database=db)
users.insert({"id": 3}, database=db)

print("All users:")
print([row._data for row in users])

# запит
result = Query(users).where("id", ">", 1).execute()

print("\nFiltered users (id > 1):")
print([row._data for row in result])

# агрегатний запит (COUNT)
count_result = Query(users).select([Count("id")]).execute()

print("\nTotal users count:")
print(count_result)

