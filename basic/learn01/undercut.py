#undercut.py 
import random 
class Player:
    def __init__(self,name = '',score = 0):
        self._name = name 
        self._score = score
    
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

class Human(Player):
    def __repr__(self):
        return "Human(%s)" % str(self)
    def get_move(self):
        while True:
            try:
                n = int(input('%s move (1-10): ' % self.get_name()))
                if 1 <= n <= 10:
                    return n
                else:
                    print('Oops!')
            except:
                print('Oops!')
            
class Computer(Player):
    def __repr__(self):
        return 'Computer(%s)' % str(self)
    def get_move(self):
        return random.randint(1,10)
 
def play_undercut(p1,p2):
    p1.reset_score()
    p2.reset_score()
    m1 = p1.get_move()
    m2 = p2.get_move()
    print("%s move: %s" % (p1.get_name(),m1))
    print("%s move: %s" % (p2.get_name(),m2))
    if m1 == m2 - 1:
        p1.incr_score()
        return p1,p2,'%s wins!' % p1.get_name()
    elif m2 == m1 - 1:
        p2.incr_score()
        return p1,p2,'%s wins!' % p2.get_name()
    else:
        return p1,p2,'draw: no winner' 
  
c = Computer('Hal Bot')
h = Human('Lia')
print(play_undercut(c,h))
c1 = Computer('Hal Bot')
c2 = Computer('MCP Bot')
print(play_undercut(c1, c2))
h1 = Human('Bea')
h2 = Human('Dee')
print(play_undercut(h1, h2))
