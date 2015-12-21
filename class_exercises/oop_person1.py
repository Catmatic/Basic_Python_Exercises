class person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def birthday(self):
        print("Congratulations! You survived another 365 days!")
        self.age += 1
