class Shoe:
    def __init__(self, shoe_type, shoe_style, color, price, label, size):
        self.shoe_type = shoe_type
        self.shoe_style = shoe_style
        self.color = color
        self.price = price
        self.manufacturer = label
        self.size = size

    def get_shoe_type(self):
        return self.shoe_type

    def get_shoe_style(self):
        return self.shoe_style

    def get_color(self):
        return self.color

    def get_price(self):
        return self.price

    def get_manufacturer(self):
        return self.manufacturer

    def get_size(self):
        return self.size


class ShoeController:
    def __init__(self):
        self.shoes = []

    def add_shoe(self, shoe):
        self.shoes.append(shoe)

    def remove_shoe(self, shoe):
        self.shoes.remove(shoe)

    def get_all_shoes(self):
        return self.shoes


class ShoeView:
    def show_shoes(self, shoes):
        for shoe in shoes:
            print("Type: ", shoe.get_shoe_type())
            print("Style: ", shoe.get_shoe_style())
            print("Color: ", shoe.get_color())
            print("Price: ", shoe.get_price())
            print("Manufacturer: ", shoe.get_manufacturer())
            print("Size: ", shoe.get_size())
            print("")


checker = ShoeController()
shoe1 = Shoe("Мужская", "Кроссовки", "Черные", 100, "LV", 42)
shoe2 = Shoe("Женская", "Туфли", "Красные", 80, "Dior", 38)
shoe3 = Shoe("Мужская", "Кроссовки", "Коричневые", 120, "Jordan", 44)
checker.add_shoe(shoe1)
checker.add_shoe(shoe2)
checker.add_shoe(shoe3)
view = ShoeView()
view.show_shoes(checker.get_all_shoes())