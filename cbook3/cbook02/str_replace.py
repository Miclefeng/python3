# str_replace.py
text = 'yeah,but no,but yeah,but no,but yeah'
print(text.replace('yeah','yep'))
texts = 'today is 11/16/2015.pycon starts 3/13/2013'
import re
print(re.sub(r'(\d+)/(\d+)/(\d+)',r'\3-\1-\2',texts))
# \3 is position 3 in r() 
# today is 2015-11-16.pycon starts 2013-3-13
from calendar import month_abbr
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
def change_date(m):
	mon_name = month_abbr[int(m.group(1))]
	return '{} {} {}'.format(m.group(2),mon_name,m.group(3))
print(datepat.sub(change_date,texts))
# today is 16 Nov 2015.pycon starts 13 Mar 2013
text3 = 'today is 11/16/2015,next is 12/16/2015,last is 11/15/2015'
newtxt,n = datepat.subn(r'\3-\1-\2',text3)
print(newtxt,n) # replace counts
# today is 2015-11-16,next is 2015-12-16,last is 2015-11-15 			3