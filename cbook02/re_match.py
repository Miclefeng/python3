# re_match.py
text1 = '11/27/2012'
text2 = 'Nov 27, 2012'
import re

def re_match(text):
	if re.match(r'\d+/\d+/\d+',text):
		print('yes')
	else:
		print('no')

def re_datepat(datepat,text):
	if datepat.match(text):
		print('success')
	else:
		print('error')
if __name__ == '__main__':
	re_match(text1)
	re_match(text2)
	datepat = re.compile(r'\d+/\d+/\d+')
	re_datepat(datepat,text1)
	re_datepat(datepat,text2)
	text3 = 'Today is 11/16/2015. PyCon starts 08/08/2008'
	print(datepat.findall(text3))
	# ['11/16/2015', '08/08/2008']

	datepats = re.compile(r'(\d+)/(\d+)/(\d+)')
	m = datepats.match('11/16/2015')
	print(m.group(0))	# 11/16/2015
	print(m.group(1))	# 11
	print(m.groups())	# ('11', '16', '2015')
	print(datepats.findall(text3))
	# [('11', '16', '2015'), ('08', '08', '2008')]
	month,day,year = m.groups()

	for month,day,year in datepats.findall(text3):
		print('{0}-{1}-{2}'.format(month,day,year))
	# 11-16-2015
	# 08-08-2008

