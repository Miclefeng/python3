# mylist.py
values = ['1','2','-3','-','4','N/A','5']

def is_int(val):
	try:
		x = int(val)
		return x
	except ValueError:
		return False

ivals = list(filter(is_int,values))
print(ivals)
# ['1', '2', '-3', '4', '5']   is filter
ivals2 = list(map(is_int,values))
print(ivals2)
# [1, 2, -3, False, 4, False, 5] not filter