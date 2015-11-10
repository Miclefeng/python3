# callback.py
from tkinter import Button
class Callback:
	def __init__(self,color):
		self.color = color
	def __call__(self):
		print('turn',self.color)

cb1 = Callback('blue')
cb2 = Callback('green')

b1 = Button(command=cb1)
b2 = Button(command=cb2)
cb1()
cb2()
cb3 = (lambda color='red':'turn ' + color)
print(cb3())

