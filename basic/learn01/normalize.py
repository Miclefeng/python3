# normalize.py 

keep = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ',"'",'-'}
def normalize(s):
    """ Convert s to a normalized string """
    result = ''
    for c in s.lower():
        if c in keep:
            result += c
    return result

def normalize2(s):
    """ Convert s to normalized string. """
    return ''.join(c for c in s.lower() if c in keep)

def file_stats(fname):
    s = open(fname,'r').read()
    num_chars = len(s)
    num_lines = s.count('\n')
    num_words = len(normalize(s).split())
    
    print(normalize(s))
    print("The file '%s' has: " % fname)
    print(" %s characters" % num_chars)
    print(" %s lines" % num_lines)
    print(" %s words" % num_words)

file_stats('story.txt')
    
