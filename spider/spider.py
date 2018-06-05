import re
from urllib import request


class Spider():
    # beautifulsoup scrapy
    url = 'https://www.panda.tv/cate/lol'
    root_pattern = '<div\s*class="video-info">([\s\S]*?)</div>'
    name_pattern = '<span\s*class="video-title"\s*title="(.*?)">'
    number_pattern = '<span\s*class="video-number">([\s\S]*?)</span>'

    @staticmethod
    def __fetch_content():
        req = request.urlopen(Spider.url)
        htmls = req.read()
        htmls = str(htmls, encoding='utf-8')
        return htmls

    @staticmethod
    def __analysis(htmls):
        root_htmls = re.findall(Spider.root_pattern, htmls)
        anchors = []
        for html in root_htmls:
            name = re.findall(Spider.name_pattern, html)
            number = re.findall(Spider.number_pattern, html)
            anchor = {'name': name, 'number': number}
            anchors.append(anchor)
        return anchors

    @staticmethod
    def __refine(anchors):
        formating = lambda anchor: {
            'name': anchor['name'][0].strip(),
            'number': anchor['number'][0]
        }
        return map(formating, anchors)

    def __sort(self, anchors):
        anchors = sorted(anchors, key=self.__sort_seed, reverse=True)
        return anchors

    @staticmethod
    def __sort_seed(anchor):
        res = re.findall('\d*', anchor['number'])
        number = float(res[0])
        if '万' in anchor['number']:
            number *= 10000
        return number

    @staticmethod
    def __show(anchors):
        for i in range(0, len(anchors)):
            print(
                'Rank' + str(i + 1)
                + ' : ' + anchors[i]['name']
                + '    ' + anchors[i]['number']
            )

    def go(self):
        htmls = self.__fetch_content()
        anchors = self.__analysis(htmls)
        anchors = list(self.__refine(anchors))
        anchors = self.__sort(anchors)
        self.__show(anchors)


spider = Spider()
spider.go()
