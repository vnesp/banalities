from .abstract_object import AbstractObject

class User (AbstractObject):

    table = 'user'
    fields = ['id', 'full_name', 'nick_name']

    def __init__(self, _id: int = None, full_name: str = None, nick_name: str = None):
        if full_name is None and nick_name is None:
            super().__init__(_id)
        else:
            super().__init__(_id, values = (full_name, nick_name))

