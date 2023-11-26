# --- Бинарное дерево ---

# class Node:
#
#     def __init__(self, value, right=None, left=None):
#         self.value = value
#         self.right = right
#         self.left = left
#
#
# class BinaryTree:
#
#     def __init__(self, root):
#         self.root = root
#
#     def bfs(self, node):  # Обход в ширину по дереву (Breadth-first-search),
#         # используется, чтобы найти самый короткий путь до значения
#         if node is None:
#             return
#
#         queue = [node]
#         while queue:
#             print('')
#             new_level = []
#             for i_node in queue:
#                 print(i_node.value, end=' ')
#                 if i_node.left:
#                     new_level.append(i_node.left)
#                 if i_node.right:
#                     new_level.append(i_node.right)
#             queue = new_level
#
#     def dfc(self, node):  # обход в глубину по дереву (Depth-first-search)
#         # нужен, чтобы искать есть ли путь до значения, идет слева-направо в глубину
#         if node is None:
#             return
#         self.dfc(node.left)
#         print(node.value)
#         self.dfc(node.right)
#
#     # Найти минимальную глубину дерева
#     def min_depth(self):
#         if not self.root:
#             return 0
#         queue = [self.root]
#         cur_level = 0
#         while queue:
#             cur_level += 1
#             for i_node in range(len(queue)):
#                 cur_node = queue.pop(0)
#                 if cur_node.left or cur_node.right:
#                     if cur_node.left:
#                         queue.append(cur_node.left)
#                     if cur_node.right:
#                         queue.append(cur_node.left)
#                 else:
#                     return cur_level
#         return cur_level
#
#
# root = Node(10)
#
# node_1 = Node(5)
# root.left = node_1
#
# node_2 = Node(7)
# node_1.right = node_2
#
# node_3 = Node(16)
# root.right = node_3
#
# node_4 = Node(13)
# node_3.left = node_4
#
# node_5 = Node(2)
# node_1.left = node_5
#
# node_6 = Node(20)
# node_3.right = node_6
#
# node_7 = Node(1)
# node_5.left = node_7
#
# # print(root.value, root.right.value, root.left.value)
# # print(node_1.value, node_1.right.value, node_1.left.value)
# # print(node_3.value, node_3.right.value, node_3.left.value)
#
# b_tree = BinaryTree(root)
# # b_tree.bfs(root)
#
# # b_tree.dfc(root)
#
# print(b_tree.min_depth())



import hashlib
import json
import requests

# correct_hash = '0cb1fa043915114586bd559e6f84166d3e4982e9b92cbb0a6bac7a72d4671b98'
#
#
# hash_function = hashlib.sha256()  # выбрали алгоритм
# string = '0998'
# hash_function.update(string.encode())  # захешировали
# hashed_string = hash_function.hexdigest()
# print(hashed_string == string)  # вывели результат



# correct_password = '33f9f70a648de7578fc92f25e69c17a3af059d2dc44f22268e6443c45ff3be44'
#
# def hash_pass(password):
#     hash_function = hashlib.sha256()  # выбрали алгоритм
#     hash_function.update(password.encode())  # захешировали
#     hashed_string = hash_function.hexdigest()
#     return hashed_string
#
#
# password = input('Введите пароль: ')
#
# if hash_pass(password) == correct_password:
#     print('Success')
# else:
#     print('Denied')





def hash_pass(password):
    hash_function = hashlib.sha256()  # выбрали алгоритм
    hash_function.update(password.encode())  # захешировали
    hashed_string = hash_function.hexdigest()
    return hashed_string

def set_user_data(email, password):
    user_data = {'email': email, 'password': hash_pass(password)}
    return user_data

def add_new_user_to_file(user):
    with open('users.json', 'r') as file:
        users_list = json.loads(file.read())
        users_list.append(user)
    with open('users.json', 'w') as file:
        file.write(json.dumps(users_list, indent=4))  # преобразование питона в json

def get_user_by_email(email):
    with open('users.json', 'r') as file:
        users_list = json.loads(file.read())
        for i_user in users_list:
            if i_user['email'] == email:
                password = input('Введите пароль: ')
                if hash_pass(password) == i_user['password']:
                    print('Success Permission')
                    return
                else:
                    print('Permission Denied!')
                    choice = input('Восстановить пароль y/n: ')
                    if choice == 'y':
                        new_password()
        print('Пользователь не найден')
        return

def new_password():
    with open('users.json', 'r') as file:
        users_list = json.loads(file.read())
        email = input('Введите email: ')
        for i_user in users_list:
            if i_user['email'] == email:
                new_pass = input('Введите новый пароль: ')
                with open('users.json', 'w'):
                    




get_user_by_email('test@mail.ru')


user = set_user_data('test@mail.ru', 'hello')
add_new_user_to_file(user)

user_2 = set_user_data('Haha@mail.ru', 'goodbye')
add_new_user_to_file(user_2)




# JSON

# import pprint
# import requests
# import json
#
# response = requests.get('https://swapi.dev/api/people/1/')
# data = json.loads(response.text)
# print(data['name'])



















































