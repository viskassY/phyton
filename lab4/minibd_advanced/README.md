ОПИС ПРОЄКТУ 

MiniDB Advanced — це реалізація міні-рушія реляційної бази даних у пам’яті, написаного на Python з використанням об’єктно-орієнтованого програмування.

Проєкт підтримує:

створення таблиць,
CRUD-операції,
перевірку цілісності даних,
виконання запитів (query engine),
транзакції з rollback,
агрегації та group by.ю


СТРУКТУРА ПРОЄКТУ

minidb_advanced/ 
├── minidb/ 
│ ├── core/ 
│ │ ├── datatypes.py 
│ │ ├── column.py 
│ │ ├── row.py
│ │ └── table.py 
│ ├── query/ 
│ │ ├── engine.py 
│ │ ├── conditions.py 
│ │ └── joined_table.py 
│ ├── transaction.py 
│ └── database.py 
├── tests/ 
|    ├── test_column.py
|    ├── test_database.py
|    ├── test_join.py
|    ├── test_query.py
|    ├── test_row.py
|    ├── test_table.py
|    ├── test_transaction.py
├── examples /
└── README.md


ОСНОВНІ КОМПОНЕНТИ

DataType

Абстрактний клас для типів даних (Integer, String, Float тощо).
Відповідає за валідацію значень.


Column

Описує колонку таблиці:
  тип даних
  nullable
  unique
  foreign key


Row
  Представляє один рядок таблиці.
  Дані зберігаються у вигляді словника.

Table
Керує даними таблиці:
  insert, update, delete
  перевірка обмежень
  індексація для unique полів


Query Engine
Реалізує виконання запитів:
  select
  where
  order_by
  limit, offset
  group_by
  агрегатні функції


JoinedTable
  Реалізує INNER JOIN між двома таблицями.

Database

Центральний клас:
  зберігає таблиці
  керує транзакціями
  виконує серіалізацію (JSON)


Transaction

Контекстний менеджер:
  commit при успіху
  rollback при помилці

Агрегації
  Підтримуються:
  COUNT
  SUM
  AVG
  MAX
  MIN
З можливістю групування


Class Design Decisions

1. Використання ООП
Проєкт побудований на принципах ООП:
  DataType — абстракція типів
  Table — координатор даних
  Database — фасад

2. Валідація через Column
Логіка перевірки винесена в Column, що забезпечує:
  повторне використання
  чисту архітектуру

3. Transaction через deepcopy
Rollback реалізовано через створення повної копії стану бази:
  проста реалізація
  гарантія відновлення

4. Query Engine
Реалізовано через method chaining:
  гнучкість
  зрозумілий синтаксис

5. Group By + Aggregation
Агрегації виконуються після групування, що повторює логіку SQL.