class Builder:
    def __init__(self):
        self.product = Product()

    def build_part_a(self):
        self.product.add("Part A")

    def build_part_b(self):
        self.product.add("Part B")

    def build_part_c(self):
        self.product.add("Part C")

    def get_product(self):
        return self.product


class Product:
    def __init__(self):
        self.parts = []

    def add(self, part):
        self.parts.append(part)

    def show(self):
        print("Product parts: ")
        for part in self.parts:
            print(part)


# Тестируем работу созданного класса
builder = Builder()
builder.build_part_a()
builder.build_part_b()
builder.build_part_c()
product = builder.get_product()
product.show()