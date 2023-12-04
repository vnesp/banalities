# Телеграм-бот для игры в банальности

* `create_base.sql` - sql-скрипт для создания базы
* `dao` - data access object
  * `base.py` - объект базы

Создание базы

``` bash
sqlite3 base.db < create_base.sql
```

Запуск

``` bash
python main.py
```
