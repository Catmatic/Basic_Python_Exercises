from datetime import datetime 

class person(object):
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday

    #takes a datetime and returns age
    def age(self, time=datetime.now()):
        difference = time - self.birthday
        return round(((difference.days)/365), 2)

Ethan = person("Ethan", datetime(1984, 1, 1))

print(Ethan.name, Ethan.birthday)
print(Ethan.age())
#in order for the function to understand that a datetime is being input,
#you must call datetime() to convert from int!
print(Ethan.age(datetime(1995,11,12)))
