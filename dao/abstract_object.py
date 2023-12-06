from .base import base
from typing import Dict, List, Tuple, Any

class AbstractObject:

    @classmethod
    def getTable(cls) -> str:
        return cls.table


    @classmethod
    def getFields(cls) -> List[str]:
        return cls.fields


    def __str__(self):
        return str(self.getObj())


    def getTuple(self) -> Tuple[Any]:
        return tuple(map(
            lambda field: getattr(self, field),
            self.getFields()
        ))


    def getObj(self) -> Dict[str, Any]:
        return dict(map(
            lambda field: (field, getattr(self, field)),
            self.getFields()
        ))


    def setFromTuple(self, values: Tuple[Any]) -> None:
        for field, value in zip(self.getFields(), values):
            setattr(self, field, value)
        self.valid = True


    def setFromObj(self, obj: Dict[str, Any]) -> None:
        for field in self.getFields():
            setattr(self, field, obj.get(field))
        self.valid = True


    def __init__(self, _id: int = None, obj: Dict[str, Any] = None, values: Tuple[Any] = None):
        self.updated = {}
        self.deleted = False
        if obj is not None:
            if _id is not None:
                obj.update('id', _id)
            self.setFromObj(obj)
            base.putObj(self.getTable(), obj)
            self.id = base.getCursor().lastrowid
        elif values is not None:
            if _id is not None:
                values = (_id, ) + values[-len(self.getFields()) + 1: ]
            base.put(self.getTable(), values, self.getFields()[-len(values): ])
            self.setFromTuple((base.getCursor().lastrowid, ) + values[-len(self.getFields()) + 1: ])
        else:
            self.id = _id
            self.valid = False


    def read(self) -> None:
        result = base.getById(self.getTable(), self.id)
        self.setFromTuple(result)
        self.valid = True
        self.deleted = False
        self.updated = {}


    def undo(self) -> None:
        if len(self.updated) == 0:
            return
        self.read()


    def delete(self) -> None:
        self.updated = {}
        self.deleted = True
        self.valid = False


    def update(self, field: str, value: Any) -> None:
        setattr(self, field, value)
        self.updated[field] = value
        

    def update(self, obj: Dict[str, Any]) -> None:
        self.setFromObj(obj)
        self.updated.update(obj)


    def flush(self) -> None:
        if self.deleted:
            base.delById(self.getTable(), self._id)
            self.valid = False
        if len(self.updated) != 0:
            base.updateById(self.getTable(), self._id, self.updated)
            self.updated = {}


    def __del__(self):
        self.flush()
