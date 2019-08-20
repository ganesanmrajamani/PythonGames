import random

class Book:
        def turn(self):
                turnrun = random.randint(0,6)
                self.score += turnrun
                print(f'{self.name} got {turnrun} and the score is {self.score}')
                pass

class Player(Book):
        def __init__ (self, name):
                self.name = name
                self.score = 0
                print (f'Welcome {self.name}')

def print_result(p1score, p2score):
        if p1score >p2score:
                print(f'{p1.name} won')
        else:
                print(f'{p2.name} won')
        print(f'{p1.name} score: {p1score}\n{p2.name} score: {p2score}')


p1 = input('Enter Player 1 name: ').title()
p1 = Player(p1)
p2 = input('Enter Player 2 name: ').title()
p2 = Player(p2)
p1.chance = True


# Match continues until one of the player reaches score 100
# The first player who achieves a score of 100 wins
# Player gets another chance if a 6 is hit

while max(p1.score,p2.score) <= 100:

        while p1.chance:
                p1run = p1.turn()
                p1.chance = (6 == p1run)
        p2.chance = True

        while p2.chance:
                p2run = p2.turn()
                p2.chance = (6 == p2run)
        p1.chance = True

print_result(p1.score, p2.score)
