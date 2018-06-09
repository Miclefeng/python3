#=============================================================
# File Name: manual_iter.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: Fri 08 Jun 2018 11:39:15 AM CST
#=============================================================
# coding:utf8

def manual_iter():
    with open('/etc/passwd') as f:
        try:
            while True:
                line = next(f)
                print(line, end='')
        except StopIteration:
            pass

def manual_iterator():
    with open('/etc/passwd') as f:
        while True:
            line = next(f, None)
            if line is None:
                break
            print(line, end='')

manual_iter()
print('\n')
manual_iterator()
print('\n')

class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_child(self, node):
        self._children.append(node)
    # 对对象进行迭代是 调用 对象内部的 __iter__方法
    # __iter__() 方法只是简单的将迭代请求传递给内部的 _children 属性
    def __iter__(self):
        return iter(self._children)

if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    # output Node(1) Node(2)
    for ch in root:
        print(ch)
