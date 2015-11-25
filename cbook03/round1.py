# round.py
from decimal import Decimal
from decimal import localcontext
a = 4.2
b = 2.1
print(a + b)
# 6.300000000000001

a = Decimal('4.2')
b = Decimal('2.1')
print(a + b)
# 6.3

a = Decimal('1.3')
b = Decimal('1.7')
print(a / b)
# 0.7647058823529411764705882353

with localcontext() as ctx:
	ctx.prec = 4
	print(a / b)
	# 0.7647

import math
nums = [1.28e+18,1,-1.28e+18]
print(sum(nums))		# 0.0
print(math.fsum(nums))	# 1.0


