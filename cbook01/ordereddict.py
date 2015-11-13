# ordereddict.py
from collections import OrderedDict
d = OrderedDict()
d['foo'] = 1
d['bar'] = 4
d['spam'] = 3
d['grok'] = 2

for key in d:
	print(key,d[key])
# foo 1
# bar 4
# spam 3
# grok 2
import json
print(json.dumps(d))
# {"foo": 1, "bar": 2, "spam": 3, "grok": 4}

