# переписать с гитхаба
# class Pizza:
#     def __init__(self, name):
#         self.name = name
#         self.toppings = []
#
#     def add_topping(self, topping):
#         self.toppings.append(topping)
#
#     def get_description(self):
#
#
# class Order:
#     def __init__(self):
#         self.pizzas = []
#         self.status = 'In Progress'
#
#     def add_pizza(self, pizza):
#
#
#     def calculate_total(self):
#         return 100 * len(self.pizzas)
#
#     def complete_order(self):
#         self.status = 'Completed'
#         return f'Order completed. Total cost: {self.calculate_total()}'
#
# class Payment:
#     @staticmethod
#     def process_payment(amount):
#         print(f'Payment of {amount} rub. successfully processed')
#
#
#
# class Report:
#     @staticmethod
#     def generate_sales_report(orders):
#         total_sales = sum(order.calculate_total() for order in orders)
#         print(f'Total sales volume: {total_sales} rub.')





# Задача по работе с дробями

# from fractions import Fraction
# import unittest
#
# class FractionCalculator:
#     def __init__(self, numerator, denominator):
#         self.fraction = Fraction(numerator, denominator)
#
#     def __add__(self, other):
#         return self.fraction + other.fraction
#
#     def __sub__(self, other):
#         return self.fraction - other.fraction
#
#     def __mul__(self, other):
#         return self.fraction * other.fraction
#
#     def __divmod__(self, other):
#         return self.fraction / other.fraction
#
#
# class TestFractionCalculator(unittest.TestCase):
#     def test_add(self):
#         frac_1 = FractionCalculator(1, 2)
#         frac_2 = FractionCalculator(1, 4)
#         self.assertEqual(frac_1.__add__(frac_2), Fraction(3, 4))
#
#     def test_sub(self):
#         frac_1 = FractionCalculator(1, 2)
#         frac_2 = FractionCalculator(1, 4)
#         self.assertEqual(frac_1.__sub__(frac_2), Fraction(1, 4))
#
#     def test_mul(self):
#         frac_1 = FractionCalculator(1, 2)
#         frac_2 = FractionCalculator(1, 4)
#         self.assertEqual(frac_1.__mul__(frac_2), Fraction(1, 8))
#
#     def test_div(self):
#         frac_1 = FractionCalculator(1, 2)
#         frac_2 = FractionCalculator(1, 4)
#         self.assertEqual(frac_1.__divmod__(frac_2), Fraction(2))





import unittest

class NumCalculator:
    def __init__(self, nums):
        self.nums = nums

    def __add__(self, other):
        return self.nums + other.nums

    def __sub__(self, other):
        return self.nums - other.nums

    def __mul__(self, other):
        return self.nums * other.nums

    def __divmod__(self, other):
        return self.nums / other.nums

    def max(self, other):
        return max(self.nums, other.nums)

    def min(self, other):
        return min(self.nums, other.nums)

    def percent(self, other):
        return (self.nums / other.nums) * 100

    def degree(self, other):
        return self.nums ** other.nums


class TestNumCalculator(unittest.TestCase):
    def test_add(self):
        num_1 = NumCalculator(2)
        num_2 = NumCalculator(1)
        self.assertEqual(num_1.__add__(num_2), 3)

    def test_sub(self):
        num_1 = NumCalculator(2)
        num_2 = NumCalculator(1)
        self.assertEqual(num_1.__divmod__(num_2), 2)

    def test_mul(self):
        num_1 = NumCalculator(2)
        num_2 = NumCalculator(1)
        self.assertEqual(num_1.__mul__(num_2), 2)

    def test_div(self):
        num_1 = NumCalculator(2)
        num_2 = NumCalculator(1)
        self.assertEqual(num_1.__divmod__(num_2), 2.0)

    def test_max(self):
        num_1 = NumCalculator(2)
        num_2 = NumCalculator(1)
        self.assertEqual(num_1.max(num_2), 2)

    def test_min(self):
        num_1 = NumCalculator(2)
        num_2 = NumCalculator(1)
        self.assertEqual(num_1.min(num_2), 1)

    def test_percent(self):
        num_1 = NumCalculator(2)
        num_2 = NumCalculator(1)
        self.assertEqual(num_1.percent(num_2), 200)

    def test_degree(self):
        num_1 = NumCalculator(2)
        num_2 = NumCalculator(1)
        self.assertEqual(num_1.degree(num_2), 2)























