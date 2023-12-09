import copy

class Prototype:
    def clone(self):
        return copy.deepcopy(self)


class ConcretePrototype(Prototype):
    def __init__(self, name):
        self.name = name

    def show(self):
        print("Name: " + self.name)


# Тестируем работу созданного класса
prototype = ConcretePrototype("Prototype")
clone = prototype.clone()
clone.show()
