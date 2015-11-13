# sorteddict.py
from operator import itemgetter

rows = [{'x':'abc','y':'jones','n':1003},
		{'x':'cba','y':'mike','n':1002},
		{'x':'bca','y':'clease','n':1001},
		{'x':'cca','y':'jones','n':1004}]
row_x = sorted(rows,key=itemgetter('x'))
print(row_x)
print(sorted(rows,key= lambda x:x['x']))
# [{'n': 1003, 'x': 'abc', 'y': 'jones'}, {'n': 1001, 'x': 'bca', 'y': 'clease'}, {'n': 1002, 'x': 'cba', 'y': 'mike'}, {'n': 1004, 'x': 'cca', 'y': 'jones'}]
row_y_x = sorted(rows,key=itemgetter('y','x'))
print(row_y_x)
print(sorted(rows,key= lambda x:(x['y'],x['x'])))
# [{'y': 'clease', 'n': 1001, 'x': 'bca'}, {'y': 'jones', 'n': 1003, 'x': 'abc'}, {'y': 'jones', 'n': 1004, 'x': 'cca'}, {'y': 'mike', 'n': 1002, 'x': 'cba'}]

# print(sorted({'q':4,'w':3,'e':5,'r':1}))
class User:
	def __init__(self, user_id):
		self.user_id = user_id

	def __repr__(self):
		return 'User({0})'.format(self.user_id)

from operator import attrgetter
user = [User(23),User(3),User(99)]
print(sorted(user,key=lambda u:u.user_id))
# [User(3), User(23), User(99)]
print(sorted(user,key=attrgetter('user_id'))) # this.speed > lambda.speed
# [User(3), User(23), User(99)]




