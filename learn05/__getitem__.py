# __getitem__.py
class Indexer:
	def __getitem__(self,index):
			return index ** 2

x = Indexer()
print(x[2])

for i in range(5):
	print(x[i],end=' ')

print('\n')

class Index:
	data = [5,6,7,8,9]
	def __getitem__(self,index):
		print('getitem:',index,'\n')
		return self.data[index]
y = Index()
print(y[0])
print(y[1])
print(y[-1])
print(y[2:4])
print(y[::2])