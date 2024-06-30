import random
import time
class CorrectChair:
    '''a chair for a chairlift'''
    max_occupants = 4
    def __init__(self,id):
        self.id = id
        self.count = 0
    def load(self,number):
        new_val = self._check(self.count + number)
        self.count = new_val
    def unload(self,number):
        new_val = self._check(self.count-number)
        self.count = new_val
    def _check(self,number):
        if number<0 or number> self.max_occupants:
            raise ValueError('Invalid count {}'.format(number))
        return number
NUM_CHAIRS = 20
chairs = []
for num in range(1,NUM_CHAIRS+1):
    chairs.append(CorrectChair(num))
def avg(chairs):
    total = 0
    for c in chairs:
        total+=c.count
    return total/len(chairs)
in_use = []
transported = 0
while True:
    if len(in_use) > NUM_CHAIRS / 2:
        transported += loading.count
        unloading = in_use.pop(0)
        print('Unloading Chair {} Count: {} Avg: {:.2} Total: {}'.format(unloading.id,unloading.count,avg(in_use), transported))
        unloading.unload(unloading.count)
        chairs.append(unloading)
    else:
        loading = chairs.pop(0)
        in_use.append(loading)
        in_use[-1].load(random.randint(1,4))
        print('Loading Chair {} Count: {} Avg: {:.2} Total: {}'.format(loading.id,loading.count,avg(in_use), transported))
    time.sleep(.25)

