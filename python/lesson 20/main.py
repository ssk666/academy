# Структуры данных


# class Queue:
#     """
#     # FIFO First In First Out
#     """
#     def __init__(self):
#         self.queue = []
#
#     def add_item(self, item):
#         self.queue.append(item)
#
#     def pop_item(self):
#         if self.queue:
#             self.queue.pop(0)
#
#     def show_queue(self):
#         print(f'Очередь: {self.queue}')


# queue = Queue()
# queue.show_queue()
# queue.add_item(5)
# queue.add_item(4)
# queue.show_queue()
# queue.pop_item()
# queue.show_queue()



# class Stack:
#     """
#     LIFO Last In First Out
#     """
#     def __init__(self):
#         self.stack = []
#
#     def add_item(self, item):
#         self.stack.append(item)
#
#     def pop_item(self):
#         if self.stack:
#             self.stack.pop(-1)
#
#     def show_stack(self):
#         print(f'Очередь: {self.stack}')


# stack = Stack()
# stack.show_stack()
# stack.add_item(5)
# stack.add_item(4)
# stack.add_item(3)
# stack.show_stack()
# stack.pop_item()
# stack.show_stack()



# class Node:
#
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next
#
#
# class LinkedList:
#
#     def __init__(self, head):
#         self.head = head
#
#     def get_all_nodes(self):
#         current = head
#         while current:
#             yield current.value
#             current = current.next
#
#     def remove_node(self, value):
#         current = head
#         prev = current
#         while current:
#             if current.value == value:
#                 prev.next = current.next
#                 return
#             prev = current
#             current = current.next


# head = Node(1)  # головной узел
# node_1 = Node(2)  # создали новый узел
# head.next = node_1  # привязали первый узел к головному

# node_2 = Node(3)  # создали новый узел
# node_1.next = node_2  # привязали второй узел к первому

# print(head.value, head.next.value, head.next.next.value)

# linked_list = LinkedList(head)
# linked_list.get_all_nodes()  # вывод всех узлов

# linked_list = LinkedList(head)
# linked_list.get_all_nodes()
#
# linked_list.remove_node(3)
# for i in linked_list.get_all_nodes():
#     print(i)



#  Посчитать сколько услов в связанном списке

class Node:

    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:

    def __init__(self, head):
        self.head = head

    def get_all_nodes(self):
        current = self.head
        while current:
            yield current.value
            current = current.next

    def remove_node(self, value):
        current = head
        prev = current
        while current:
            if current.value == value:
                prev.next = current.next
                return
            prev = current
            current = current.next

    def get_count(self):
        count = 0
        current = head
        while current:
            count += 1
            current = current.next
        return count

    def get_center(self):
        current = head
        for i in range(self.get_count() // 2):
            current = current.next
        return current.value

    def get_num(self, num):
        current = head
        for num in range(num):
            current = current.next
        return current.value

    def change_node(self, num_node):
        node = Node(num_node)
        node.next = self.head
        self.head = node
        return node.value

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev






head = Node(0)
node_1 = Node(1)
node_2 = Node(2)
node_3 = Node(3)
node_4 = Node(55)
node_5 = Node(5)
node_6 = Node(6)
node_7 = Node(7)

head.next = node_1
node_1.next = node_2
node_2.next = node_3
node_3.next = node_4
node_4.next = node_5
node_5.next = node_6
node_6.next = node_7

linked_list = LinkedList(head)
linked_list.get_all_nodes()

# print(linked_list.get_count())
#
# print(linked_list.get_center())
#
# print(linked_list.get_num(4))

linked_list = LinkedList(head)

print(linked_list.change_node(2))

print(linked_list.get_all_nodes())



































































