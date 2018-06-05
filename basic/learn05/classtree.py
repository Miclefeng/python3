# classtree.py

# B().__class__.__bases__ goto parent object
def classtree(cls,indent):
	print('.' * indent + cls.__name__)
	for supercls in cls.__bases__:
		classtree(supercls,indent+3)

def instancetree(inst):
	print('Tree of %s' % inst)
	classtree(inst.__class__,3)

def selftest():
	class A: pass
	class B(A): pass
	class C(A): pass
	class D(B,C): pass
	class E: pass
	class F(D,E): pass
	instancetree(B())
	instancetree(F())

if __name__ == '__main__': selftest()
# instancetree(B())
# Tree of <__main__.selftest.<locals>.B object at 0x7ff1b197db00>
# ...B
# ......A
# .........object
# instancetree(F())
# Tree of <__main__.selftest.<locals>.F object at 0x7ff1b197db00>
# ...F
# ......D
# .........B
# ............A
# ...............object
# .........C
# ............A
# ...............object
# ......E
# .........object

