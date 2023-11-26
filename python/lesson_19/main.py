# class MyZeroDivisionError(BaseException):
#
#     def __init__(self, message=''):
#         self.message = message
#
#
# def divide(a, b):
#     # try:
#     #     return a / b
#     # except ZeroDivisionError:
#     #     return f'Делить на 0 нельзя'
#     # except MyZeroDivisionError as error:
#     #     print(error.message)
#     #     return error.message
#     try:
#         if b == 0:
#             raise MyZeroDivisionError('Деление на 0!')
#     except MyZeroDivisionError as error:
#         return error
#     # raise MyZeroDivisionError('Деление на 0!')  # ошибка с пояснением
#

# print(divide(10, 0))




# class Vehicle:
#
#     def __init__(self, weight):
#         self.weight = weight
#
#
# class Ship(Vehicle):
#     pass
#
#
# base_vehicle = Vehicle(1000)
# ship = Ship(1000)

# print(isinstance(base_vehicle, Vehicle))  # принадлежит ли base_vehicle к Vehicle
# print(issubclass(Ship, Vehicle))  # относится ли класс Ship к классу Vehicle




# class Multiply:
#
#     def __init__(self, num_1, num_2):
#         self.num_1 = num_1
#         self.num_2 = num_2
#
#     def __call__(self, *args, **kwargs):
#         print(f'Hey {kwargs["name"]}')
#         return self.num_1 * self.num_2
#
#
# multiply = Multiply(20, 11)
# result = multiply(name='Mara')
# print(result)



# Перегрузка операторов


# class Number:
#
#     def __init__(self, number):
#         self.number = number
#
#     def __add__(self, other):
#         if isinstance(other, Number):
#             return self.number + other.number
#         else:
#             return 'Сложение невозможно'
#
#     def __sub__(self, other):
#         if isinstance(other, Number):
#             return self.number - other.number
#         else:
#             return 'Вычитание невозможно'
#
#     def __mul__(self, other):
#         if isinstance(other, Number):
#             return self.number * other.number
#         else:
#             return 'Умножение невозможно'
#
#     def __divmod__(self, other):
#         if isinstance(other, Number):
#             return self.number % other.number
#         else:
#             return 'Деление с остатком невозможно'
#
#     def __truediv__(self, other):
#         if isinstance(other, Number):
#             return self.number / other.number
#         else:
#             return 'Деление без остатка невозможно'
#
#     def __eq__(self, other):
#         if isinstance(other, Number):
#             return self.number == other.number
#         else:
#             return 'Равно ли невозможно'
#
#     def __gt__(self, other):
#         if isinstance(other, Number):
#             return self.number > other.number
#         else:
#             return 'Сравнение невозможно'
#
#     def __ge__(self, other):
#         if isinstance(other, Number):
#             return self.number >= other.number
#         else:
#             return 'Сравнение невозможно'
#
#     def __lt__(self, other):
#         if isinstance(other, Number):
#             return self.number < other.number
#         else:
#             return 'Сравнение невозможно'
#
#     def __le__(self, other):
#         if isinstance(other, Number):
#             return self.number <= other.number
#         else:
#             return 'Сравнение невозможно'
#
#     def __ne__(self, other):
#         if isinstance(other, Number):
#             return self.number != other.number
#         else:
#             return 'Сравнение невозможно'
#
#
# number_1 = Number(10)
# number_2 = Number(11)
# result = number_1 + number_2
# print(result)



# Сбор корзины на сайте





class Item:

    def __init__(self, name, price, quantity, shop, sale=0):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.shop = shop
        self.sale = sale

    def get_total_price(self):
        return (self.price - self.price * (1 - self.sale)) * self.quantity


class Cart:

    def __init__(self):
        self.cart = []

    def __add__(self, other):
        if isinstance(other, Cart):
            # merge_cart = Cart()
            # merge_cart.cart = self.cart + other.cart
            # return merge_cart
            self.cart += other.cart
            return self
        return 'Невозможно произвести слияние корзин'


    def add_item(self, *args):
        for i_item in args:
            self.cart.append(i_item)

    def get_items(self):
        print(f'Товары в корзине: ')
        for i_item in self.cart:
            print(f'Название: {i_item.name}\nЦена: {i_item.price}\nКоличество: {i_item.quantity}\nСкидка: {i_item.sale}\n'
                  f'Магазин: {i_item.shop.name}\n'
                  f'Общая стоимость: {i_item.get_total_price()}\n'
                  f'{"":-^25}')
            print(f'Общая стоимость корзины: {self.total_cart_price()}')

    def total_cart_price(self):
        total_price = sum([i_item.get_total_price() for i_item in self.cart])
        return total_price


class Shop(Item):

    def __init__(self, name):
        self.name = name


shop_1 = Shop('Монетка')


cart_1 = Cart()
cart_1.add_item(Item('iphone', 100, 5, shop_1), Item('xiaomi', 200, 10, shop_1))
# cart_1.get_items()

# авторизованный пользователь
cart_2 = Cart()
cart_2.add_item(Item('Alex', 300, 2, shop_1), Item('Denis', 400, 20, shop_1))

# cart_2.get_items()

# cart_3 = cart_1 + cart_2
# cart_3.get_items()

cart_1 += cart_2
cart_1.get_items()
del cart_2

















