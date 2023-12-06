from dao.base import base
from dao.user import User

print(base.getTable('user'))
user = User(6, 'Виктория', 'Береника')
print(user)
"""
print(base.getTable('state'))
print(base.getTable('game'))
print(base.getById('user', 1, ['id', 'nick_name']))
print(base.getById('user', 2, ('id', 'nick_name')))
print(base.getById('user', 3, ['id', 'nick_name']))
print(base.delById('user', 2))
print(base.getById('user', 2, ('id', 'nick_name')))
base.putObj('user', {'id': 2, 'full_name': 'Ольга', 'nick_name': 'Rose1'})
print(base.getById('user', 2 ))
print(base.delById('user', 4))
base.putObjs('user', [{'id': 4, 'full_name': 'Елена'}, {'nick_name': 'AngelOK', 'full_name': '', 'id': 5}])
print(base.getTable('user'))
"""
