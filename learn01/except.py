# except.py 
def convert_to_int1(s,base):
    try:
        return int(s,base)
    except(ValueError,TypeError):
        return 'error'

def convert_to_int2(s,base):
    try:
        return int(s,base)
    except ValueError:
        return 'value error'
    except TypeError:
        return 'type error'

def convert_to_int3(s,base):
    try:
        return int(s,base)
    except:
        return 'error'
def invert(x):
    try:
        return 1 / x
    except ZeroDivisionError:
        return 'error'
    finally:
        print('invert{0} done'.format(x))