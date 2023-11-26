# ООП
import time
import random

# class Vehicle:
    # __init__ - инициализация, благодаря ему мы можем в () прописать "параметры"
    # __init__ - называется еще как "конструктор"
    # def __init__(self, name: str, weight: float, hp: int, max_speed: int):
    #     self.name = name
    #     self.car_name = name
    #     self.weight = weight
    #     self.hp = hp
    #     self.__wheel_count = 4  # задали константу
    #     self.initial_fuel = 20
    #     self.max_speed = max_speed
    #     self.__possible_barrier = ['Дерево', 'Отбойник', 'Обрыв']

        # __wheel_count - это значит, что категорически нельзя изменять
        # _wheel_count - это значит, что можно изменять, но не желательно

    # def output_info(self):
    #     print(f'Info: \n'
    #           f'Name: {self.name}\n'
    #           f'Wieght: {self.weight}\n'
    #           f'hp: {self.hp}')

    # def refuel(self, litres: float):
    #     # f = int(input('На сколько литров заправится: '))
    #     self.initial_fuel += litres
    #     print(f'Было в баке изначально {self.initial_fuel} литров, заправились на литров, итоге в баке {self.initial_fuel}')

    # def drive(self, km: int):
    #     if self.initial_fuel <= 0:
    #         print('Топливо закончилось')
    #         return
    #     self.initial_fuel -= km
    #     print(self.initial_fuel)

    # def boost(self):
    #     curr_time = 0
    #     for i in range(0, self.max_speed, 20):
    #         if random.randint(1, 10) == 5:  # это вероятность 10%, тк цифра 5 может встретиться с вероятностью 1 к 10
    #             print(f'Вы встретили {random.choice(self.__possible_barrier)} при разгоне ')
    #             return
    #         curr_time += 0.5
    #         time.sleep(0.5)
    #         print(f'Current speed: {i} km/h')
    #     print(f'Машина {self.name} достигла максимально скорости за {curr_time}')






    # @staticmethod  # чтобы не прописывать self, говорим, что литры - это self
    # def refuel(litres: float):
    #     print(f'Машина заправлена на {litres} литров')


    # def __str__(self):  # благодаря __str_ можно просто писать print(), а не vehicle_1.output_info()
    #     return (f'Name: {self.name}\n'
    #             f'Weight: {self.weight}\n'
    #             f'h/p: {self.hp}\n'
    #             f'Wheels: {self.__wheel_count}')


# vehicle_1 = Vehicle(name='Audi rs7', weight=1800, hp=770, max_speed=310)
# vehicle_1, vehicle_2 - это называется "экземпляры"
# vehicle_2 = Vehicle(name='Mersedes s63', weight=2000, hp=550)
# vehicle_1.output_info() # __init__

# print(vehicle_2)  # __str__

# vehicle_1.max_speed = 310  # добавили что-то отдельно
# print('Max speed:', vehicle_1.max_speed)  # и вывели

# vehicle_1.drive(2)
# vehicle_1.drive(2)

# vehicle_1.boost()



#  Задание


# class Human:
#     def __init__(self, name: str, birth_date: str, tel: str, city: str, country: str):
#         self.name = name
#         self.birth_date = birth_date
#         self.tel = tel
#         self.city = city
#         self.country = country
#
#     def set_name(self, value):  # установить значение
#         self.name = value
#
#     def get_name(self):  # взять значение
#         return self.name
#
#
# human = Human(name='Mara', birth_date='18.09.2002', tel='79222059292', city='Ekb', country='Russia')
# print(human.get_name())
# human.set_name('Stepka')
# print(human.get_name())



from typing import List

class Student:

    def __init__(self, name: str, group_num: str, mark_list: List[int]):
        self.name = name
        self.group_num = group_num
        self.mark_list = mark_list

    def get_avg_mark(self) -> float:
        return round(sum(self.mark_list) / len(self.mark_list), 2)

    def __str__(self):
        return f'{self.name} {self.group_num} {self.get_avg_mark()}'

students = [
    Student('Marat', '303Б', [random.randint(1, 5) for _ in range(5)]),
    Student('Stepa', '302Б', [5, 5, 5, 5, 5, 5]),
    Student('Marqal', '301Б', [2, 4, 2, 1, 1, 3]),
    Student('Matva', '303Б', [2, 1, 2, 5, 5, 5]),
    Student('Mama', '304Б', [2, 5, 5, 1, 1, 3]),
    Student('Tema', '304Б', [2, 1, 2, 1, 5, 3]),
    Student('Tima', '302Б', [4, 1, 2, 1, 1, 3]),
    Student('Tolya', '305Б', [2, 4, 2, 4, 1, 4]),
]

sorted_students = sorted(students, key=lambda x: x.get_avg_mark(), reverse=True)


for i_student in sorted_students:
    print(i_student)

































































