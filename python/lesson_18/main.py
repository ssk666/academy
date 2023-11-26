# class Point:
#     # капсом пишут только те значения, которые не изменяются (константа)
#     MIN_CORDINATA = 0
#     MAX_CORDINATA = 100
#
#     def __init__(self, x, y):
#         # self.x = x
#         # self.y = y
#         self.set_coordinates(x, y)
#
#     # @classmethod
#     # def set_square(cls, left, right):
#     #     cls.MIN_CORDINATA = left
#     #     cls.MAX_CORDINATA = right
#
#     def set_coordinates(self, x, y):
#         if self.MIN_CORDINATA <= x <= Point.MAX_CORDINATA and Point.MIN_CORDINATA <= y <= self.MAX_CORDINATA:
#             # можно хоть через self хоть через Point (тк константы доступны и так и так
#             self.x = x
#             self.y = y
#         else:
#             print('Точка лежит вне области :(')
#
#     def __setattr__(self, key, value):
#         print('Сработал __setattr__')
#         if key == 'w':
#             raise ValueError('Недопустимое значение атрибута :(')
#         object.__setattr__(self, key, value)
#
#     def __getattribute__(self, item):
#         print('Сработал метод __getattr__')
#         if item == 'x':
#             raise ValueError('У вас нет доступа к значению этого атрибута')
#         return object.__getattribute__(self, item)
#
#     def __str__(self):
#         return f'Координаты точки: x={self.x}, y={self.y}'
#
# # print(Point.__dict__)
# # point = Point(1, 2)
# # point_1 = Point(3, 4)
# # point.set_square(40, 80)
# # print(Point.__dict__)
# # print(point.MIN_CORDINATA, point_1.MIN_CORDINATA)
#
# # point_1 = Point(1, 1)
# # point_1.set_coordinates(1, 50)
# # print(point_1)
#
# point = Point(1, 2)
# print(point.y)


# Наследование


class Employee:
    ID = 0
    TAX = 0.13

    def __init__(self, email, salary):
        Employee.ID += 1
        self.id = Employee.ID
        self.email = email
        self.salary = salary

    def get_salary_per_month(self, bonus=0):
        return self.salary - self.salary * self.TAX + bonus

    def __str__(self):
        return f'id: {self.id}\nemail: {self.email}\nsalary: {self.salary}'


class Manager(Employee):
    TAX = 0.1

    def __init__(self, email, salary, employees):
        super(Manager, self).__init__(email, salary)
        self.employees = employees

    def get_employees(self):
        if self.employees:
            for i_employee in self.employees:
                print(f'id: {i_employee.id}\nemail: {i_employee.email}\nsalary: {i_employee.salary}')

    def __str__(self):
        return f'\nid: {self.id}\nemail: {self.email}\nsalary: {self.salary}\n' \
               f'Employees: {self.employees[0].email}'


class Engineer(Employee):
    TAX = 0.1
    RATE = 100

    def __init__(self, email, hours, rank):
        super(Engineer, self).__init__(email, salary=0)
        self.hours = hours
        self.rank = rank

    def get_salary_per_hour(self, hours=0):
        self.salary = (self.RATE * hours) * (1 - self.TAX)
        return self.salary

    @classmethod
    def change_rate(cls, rate):
        cls.RATE = rate

    def __str__(self):
        return f'id: {self.id}\nemail: {self.email}\nsalary: {self.salary}\nrank: {self.rank}'


engineer_1 = Engineer('eng@mail.ru', 3, 'star')
engineer_1.change_rate(1000)
engineer_1.get_salary_per_hour(3)
print(engineer_1)




# employee_1 = Employee('test@mail.ru', 100)
# manager_1 = Manager('boss@mail.ru', 1000, [employee_1])
# manager_1.get_employees()
# engineer_1 = Engineer('engineer@bk.ru', 3)
# print(engineer_1)

# print(employee_1)
# print(manager_1)

















