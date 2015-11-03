# players.py 
class Player:
    def __init__(self,name):
        self._name = name
        self._score = 0
    def reset_score(self):
        self._score = 0
    def incr_score(self):
        self._score = self._score + 1
    def get_name(self):
        return self._name 
    def __str__(self):
        return "Player(name = '%s',score = %s)" % (self._name,self._score)
    def __repr__(self):
        return str(self)
p = Player('Moe')
print(p)
p.incr_score()
print(p)
p.reset_score()
print(p)

class Human(Player):
    def __str__(self):
        return "Human(name = '%s',score = %s)" % (self._name,self._score)
h = Human('Jerry')
print(h)
class Computer(Player):
    def __str__(self):
        return "Computer(name = '%s',score = %s)" % (self._name,self._score)
c = Computer('Wow')
print(c)