import time
class timer:
	def __init__(self,func):
		self.func = func
		self.alltime = 0
	
	def __call__(self,*args,**kargs):
		start = time.clock()
		result = self.func(*args,**kargs)
		elapsed = time.clock() - start
		self.alltime += elapsed
		print('%s: %.5f, %.5f' % (self.func.__name__,elapsed,self.alltime))
		return result
@timer
def listcomp(N):
	return [x * 2 for x in range(N)]

@timer
def mapcall(N):
	return list(map((lambda x:x * 2),range(N)))

resultl = listcomp(5)	# listcomp: 0.00000, 0.00000
listcomp(50000)	# listcomp: 0.01000, 0.01000
listcomp(500000)	# listcomp: 0.04000, 0.05000
listcomp(1000000)	# listcomp: 0.09000, 0.14000
print(resultl)	# [0, 2, 4, 6, 8]
print('allTime = %s' % listcomp.alltime)
# allTime = 0.13999999999999999

print('')
resultm = mapcall(5)	# mapcall: 0.00000, 0.00000
mapcall(50000)	# mapcall: 0.01000, 0.01000
mapcall(500000)	# mapcall: 0.08000, 0.09000
mapcall(1000000)	# mapcall: 0.17000, 0.26000
print(resultm)	# [0, 2, 4, 6, 8]
print('allTime = %s' % mapcall.alltime)	# allTime = 0.26
print('map/comp = %s' % round(mapcall.alltime / listcomp.alltime,3))
# map/comp = 1.857










