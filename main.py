from dao.base import base

print(base.getTable('user'))
print(base.getTable('state'))
print(base.getTable('game'))
print(base.getById('user', 1, ['id', 'nick_name']))
print(base.getById('user', 2, ('id', 'nick_name')))
print(base.getById('user', 3, ['id', 'nick_name']))
print(base.delById('user', 2))
print(base.getById('user', 2, ('id', 'nick_name')))
base.putObj('user', {'id': 2, 'full_name': 'Ольга', 'nick_name': 'Rose1'})
print(base.getById('user', 2 ))
