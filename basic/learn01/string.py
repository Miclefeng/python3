# codesum.py 
def codesum1(s):
    """ Returns the sums of the character codes fo s. """
    total = 0;
    for c in s:
        total = total + ord(c)
    return total
print(codesum1('Hi there!'))

def codesum2(s):
    """ Return the sums of the character codes of s."""
    total = 0
    for i in range(len(s)):
        total = total + ord(s[i]) # ord()返回字符的ASCII值
    return total
print(codesum2('Hi there!'))