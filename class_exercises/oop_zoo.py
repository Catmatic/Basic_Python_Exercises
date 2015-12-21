#potential classes for zoo game:

class customer(object):
    def __init__(self, age, happiness, spending_money)
        self.age = age
        self.happiness = happiness
        self.fatigue = fatigue 
        self.spending_money = spending_money

    def mod_happiness(self, deltahappiness):
       self.happiness += deltahappiness 

    def mod_fatigue(self, deltafatigue):
       self.fatigue += deltafatigue

class souvenir(object):
    def __init__(self, saleprice, deltahappiness)
        self.saleprice = saleprice 
        self.deltahappiness = deltahappiness

    def mod_saleprice(self, saleprice):
        self.saleprice = saleprice

class animal(object):
    def __init__(self, hunger, thirst, happiness)
        self.hunger = hunger
        self.thirst = thirst
        self.happiness = happiness


class carnivore(animal):
    def __init_(self, *args, **kwargs):
        super(animal, self).__init__(*args, **kwargs)
