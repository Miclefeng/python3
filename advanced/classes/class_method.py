#=============================================================
# File Name: user.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: 2018/7/1 21:51
#=============================================================
# coding:utf8

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def tomorrow(self):
        self.day += 1

    @staticmethod
    def parse_from_string(date_str):
        year,  month, day = tuple(date_str.split('-'))
        return Date(int(year), int(month), int(day))

    @classmethod
    def from_string(cls, date_str):
        year,  month, day = tuple(date_str.split('-'))
        return cls(int(year), int(month), int(day))

    def __str__(self):
        return '{year}/{month}/{day}'.format(year=self.year, month=self.month, day=self.day)


if __name__ == '__main__':
    my_date = Date(2018, 7, 1)
    print(my_date)
    my_date.from_string('2018-07-01')
    print(my_date)
    my_date.parse_from_string('2018-07-01')
    print(my_date)
