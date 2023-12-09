class Pasta:
    def __init__(self):
        self.type = None
        self.sauce = None
        self.filling = None
        self.additions = []

    def set_type(self, pasta_type):
        self.type = pasta_type

    def set_sauce(self, sauce):
        self.sauce = sauce

    def set_filling(self, filling):
        self.filling = filling

    def add_addition(self, addition):
        self.additions.append(addition)

    def show(self):
        print("Pasta type: " + self.type)
        print("Sauce: " + self.sauce)
        print("Filling: " + self.filling)
        print("Additions: ")
        for addition in self.additions:
            print(addition)


class PastaBuilder:
    def __init__(self):
        self.pasta = Pasta()

    def build_type(self, pasta_type):
        self.pasta.set_type(pasta_type)

    def build_sauce(self, sauce):
        self.pasta.set_sauce(sauce)

    def build_filling(self, filling):
        self.pasta.set_filling(filling)

    def build_addition(self, addition):
        self.pasta.add_addition(addition)

    def get_pasta(self):
        return self.pasta


# Тестируем работу созданного класса
builder = PastaBuilder()
builder.build_type("Spaghetti")
builder.build_sauce("Tomato")
builder.build_filling("Meat")
builder.build_addition("Parmesan")
pasta = builder.get_pasta()
pasta.show()