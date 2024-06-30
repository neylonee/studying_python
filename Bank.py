import random
import time
class ClientDefault:
    max_value = 50000
    min_value = 100
    max_count_operations = 5
    rate = 93
    def __init__(self,id):
        self.id = id
        self.count_operations = 0
        self.value = 0
        self.value_rub = 0
        self.value_dol = 0
    def dol_to_rub(self,value):
        self.count_operations += 1
        self.value += value*self.rate
        self.value_rub += value*self.rate
        self.value_dol -= value
        self._check(self.value*self.rate,self.count_operations)
    def rub_to_dol(self,value):
        self.count_operations += 1
        self.value += value
        self.value_rub -= value
        self.value_dol += value//self.rate
        self._check(self.value,self.count_operations)
    def _check(self,value,operations):
        if self.max_count_operations<self.count_operations:
            raise CountError('Too many operations now: {}'.format(count_operations))
        return operations
CLIENTS_COUNT = 30
def thread(CLIENTS_COUNT):
    clients = []
    for client in range(1,CLIENTS_COUNT+1):
        clients.append(ClientDefault(client))
    return clients
def avg(clients):
    total = 0
    for c in clients:
        total += c.value
    avg = total/len(clients)
    return avg
in_use = []
served = 0
threads = 1
clients = thread(CLIENTS_COUNT)
test = ClientDefault
while True:
    in_use.append(clients.pop(0))
    for i in range(random.randint(1,in_use[-1].max_count_operations)):
        if random.randint(0,1):
            in_use[-1].rub_to_dol(random.randint(in_use[-1].min_value,in_use[-1].max_value//5))
        else:
            in_use[-1].dol_to_rub(random.randint(in_use[-1].min_value//in_use[-1].rate,(in_use[-1].max_value//in_use[-1].rate)//5))
        print('Thread: {}; Client number {}; Value: {}; Руб: {}; $: {}; avg = {:.6}'.format
              (threads,in_use[-1].id,in_use[-1].value,in_use[-1].value_rub,in_use[-1].value_dol,avg(in_use)))
        time.sleep(.1)
    served+=1
    time.sleep(.5)
    if len(clients)<=1:
        print('{} thread served'.format(threads))
        threads += 1
        clients = thread(CLIENTS_COUNT)
        time.sleep(3)


    
