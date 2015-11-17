# tarnslate1.py
s = 'python\fis\tawesome\r\n'
remap = {
	ord('\t') : ' ',
	ord('\f') : ' ',
	ord('\r') : None
}

a = s.translate(remap)
print(a)	# python is awesome

text = 'hello world'
print(text.ljust(20,'*'))	# hello world*********
print(text.rjust(20,'*'))	# *********hello world
print(text.center(20,'*'))	# ****hello world*****






