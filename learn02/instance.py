# instance.py 
class Class:
    def method(self):
        print('I have a self!')

def function():
    print("I don't...")

instance = Class()
instance.method()
instance.method = function
instance.method()

class Bird:
    song = 'Squaawk!'
    def sing(self):
        print(self.song)

bird = Bird()
bird.sing()
birdsong = bird.sing
birdsong()