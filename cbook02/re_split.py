# re_split.py
import re 

line = 'asdf fjdk; afed, fjek,asdf,  foo'
line_split = re.split(r'[;,\s]\s*',line) #  r  clone '\'
print(line_split)
# ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']
