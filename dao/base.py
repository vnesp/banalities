from typing import Optional, List, Iterable
import sqlite3

class Base:

    def __init__(self):
        self.connection = sqlite3.connect('base.db')
        self.cursor = self.connection.cursor()

    def getConnection(self) -> sqlite3.Connection:
        return self.connection

    def getCursor(self) -> sqlite3.Cursor:
        return self.cursor

    def getTable(self, table: str, fields: Iterable[str] = None) -> List[tuple]:
        self.cursor.execute(f"""
            SELECT {', '.join(fields) if fields else '*'}
                FROM {table}
        """)
        return self.cursor.fetchall()

    def getById(self, table: str, _id: int, fields: Iterable[str] = None) -> Optional[tuple]:
        self.cursor.execute(f"""
            SELECT {','.join(fields) if fields else '*'}
                FROM {table}
                WHERE id = {_id}
        """)
        return self.cursor.fetchone()

    def delById(self, table: str, _id: int):
        self.cursor.execute(f"""
            DELETE
                FROM {table}
                WHERE id = {_id}
        """)
        return self.cursor.rowcount

    def put(self, table: str, values: Iterable[any], fields: Iterable[str] = None):
        self.cursor.execute(f"""
            INSERT
                INTO {table} {f'({",".join(fields)})' if fields else ''}
                VALUES ({','.join('?' * len(fields))})
        """, tuple(values))

    def putMany(self, table: str, arrValues: Iterable[Iterable[any]], fields: Iterable[str] = None):
        self.cursor.executemany(f"""
            INSERT
                INTO {table} {f'({",".join(fields)})' if fields else ''}
                VALUES ({','.join('?' * len(fields))})
        """, arrValues)

    def putObj(self, table: str, obj: dict):
        self.put(table, obj.values(), obj.keys())

    def putObjs(self, table: str, objs: List[dict]):
        fields = list(
            set().union(
                map(
                    lambda obj: set(obj.keys()),
                    objs
                )
            )
        )
        data = map(
            lambda obj: map(
                lambda field: obj.get(field),
                fields
            ),
            objs
        )
        self.putMany(table, data, fields)
           

    def flush(self):
        self.connection.commit()

    def __del__(self):
        print('Base desctructed')
        self.flush()
        self.connection.close()

base = Base()
