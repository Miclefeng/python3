# funny.py 
import re
def is_funny(s):
    return re.match('(ha)+!+',s) != None
print(is_funny('haha!'))

pets = ('dog','cat','bird','dog')
trues = 'bird' in pets
falses = 'cow' in pets
print(trues,falses)
print(len(pets))

print(pets.count('dog'))
print(pets.index('dog')) # 从0开始
