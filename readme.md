# Телеграм-бот для игры в банальности

[Схема базы](https://dbdesigner.page.link/wFPze6amsK3jXj276)

* `create_base.sql` - sql-скрипт для создания базы
* `dao` - data access object
  * `base.py` - объект базы
  * `abstract_object.py` - базовый класс для всех моделей
  * `user.py` - модель User (пользователь)

Создание базы

``` bash
sqlite3 base.db < create_base.sql
```

Запуск

``` bash
python main.py
```
