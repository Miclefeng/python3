import re

str = '<span class="video-title" title="季中之巅 总决赛RNG vs KZ">季中之巅 总决赛RNG vs KZ</span><span class="video-number">784.1万</span><span class="video-station-info"><i class="video-station-num">382人</i></span>'
s = re.findall('<span\s*class="video-title"\s*title="(.*?)">', str)
print(s)
