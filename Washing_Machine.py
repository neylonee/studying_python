import time 
import random
class WashingMachine:
    '''basic washing machine in usual house'''
    max_strange = 100 
    def __init__(self,id):
        self.id = id 
        self.strange = 0
    def first_mode(self):
        self.strange = 50
    def second_mode(self):
        self.strange = 75
    def third_mode(self):
        self.strange = 100
    def manual_mode(self,strange):
        end_strange = self._check(self.strange+strange)
        self.strange = end_strange
    def wash(self,clothe,strange):
        print('Your clothe is washing now. Please wait')
        for i in range(strange//10):
            time.sleep(.5)
            print('Whhshshshshs...')
        if self.strange == clothe:
            print('Your clothe successfully washed')
        elif self.strange > clothe:
            print('Your clothe now small :) ')
        else:
            print('Your clothe still dirty :( ')

    def _check(self,strange):
        if self.max_strange < strange or strange<0:
            raise StrangeError('Bad strange: {}'.format(strange))
        return strange
machines = []
count_machines = 20
for c in range(1,count_machines+1):
    machines.append(WashingMachine(c))
def avg(count_machines,machines):
    total = 0
    for c in range(len(machines)):
        total += machines.strange
    return total/len(machines)
in_use = []
while True:
    in_use.append(machines.pop(0))
    clothe = random.randint(50,120)
    if clothe > 100:
        print('Our Washing machines cant wash this :( Strange is so big: {}'.format(clothe))
    elif clothe <= 100:
        in_use[-1].manual_mode(clothe)
    in_use[-1].wash(clothe,in_use[-1].strange)
        

        


