user = {
    'age':18,
    'username':'kennedy',
    'weapons':['pistol','machette'],
    'is_active':True,
    'clan':'boxi'
}

print(user.keys())
user['weapons'].append('shot_gun')
print(user)
user.update({'is_banned': False})#add new key
print(user)
user['is_banned'] = True
print(user)

user2 =user.copy()

user2.update({'age': 100, 'username': 'john'})
print(user2)
print(user)