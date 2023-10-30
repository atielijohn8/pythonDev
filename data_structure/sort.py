friends = ['Simon', 'Patty', 'Joy', 'Carrie', 'Amira', 'Chu']

new_friend = ['stanley']

friends.extend(new_friend)
print(sorted(friends))#does not modify the list
print(friends)

friends.sort()#modifies
print(friends)

