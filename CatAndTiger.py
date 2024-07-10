class Cat:
    """usual street cat"""
    max_weight = 10
    max_heigh = 0.2
    max_lendth = 1
    stamina = 50
    min_stamina = 0
    strength = 10
    def __init__(self,id):
        self.id = id
        self.spent_stamina = 0
    def bite(self):
        self._check(self.spent_stamina + 10)
        self.spent_stamina += 10
    def eat(self,food_satiety):
        self._check(self.spent_stamina - food_satiety)
        self.spent_stamina -= food_satiety
    def _check(self,stamina):
        if stamina<self.min_stamina:
            raise ValueError('You`re full. Your stamina: {}'.format(stamina))
        elif stamia > self.stamina:
            raise ValueError('You`re so tired. Your stamina: {}'.format(stamina))
        return stamina
class Tiger(Cat):
    """usual street tiger"""
    max_weight = 100
    max_heigh = 1.5
    max_lendth = 2.5
    stamina = 100
    strength = 100
    

