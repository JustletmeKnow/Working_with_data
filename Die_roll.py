from random import randint, choice
class Die():

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        roll = randint(1, self.sides)
        print(roll)

rolling = Die(20)
rolling.roll_die()

counter = 0
win = False
bilet = ['ABC3', '4325', 'JSHF', '12FD', 'KJ8L']
while win == False:
    counter += 1
    i = choice(bilet)
    if i == 'KJ8L':
        print(f'You are winner!!! Your bilet is {i}')
        win = True
    else:
        print('May be you can try later?)')
print(f'Your count attempt is {counter}')