# TODO Создайте собственную программу, работающая из командной строки и
#  позволяющую просматривать, добавлять, изменять, удалять или искать контактные данные ваших знакомых.
#  Кроме этого информация должна сохроняться на диске для последующего пользования
import os.path
import pickle
import sys
import time

class Contact:
    def __init__(self, name, surname, age, number, email):
        self.count = len(user_list)
        self.name = name
        self.surname = surname
        self.age = age
        self.number = number
        self.email = email
        print(f"{self.name} {self.surname} successfully added!")

    def user_info(self):
        print(f"{self.count}. Name: {self.name} Surname: {self.surname} Age: {self.age} "
              f"Number: {self.number} e-mail: {self.email}")

    def data(self):
        u = [self.name, self.surname, self.age, self.number, self.email]
        return u


def save_to_file(data):
    with open('Data.pickle', 'wb') as file:
        pickle.dump(data, file)


def load_from_file():
    with open('Data.pickle', 'rb') as file:
        data = pickle.load(file)
    return data

# Создаем контакт и возвращаем список с данными
def create_user():
    while True:
        try:
            user_name = input("Name: ").capitalize()
            for i in user_name:
                if not i.isalpha():
                    raise print("Name must contain only letters!")
            break
        except TypeError:
            continue
    while True:
        try:
            user_surname = input("Surname: ").capitalize()
            for i in user_surname:
                if not i.isalpha():
                    raise print("Surname must contain only letters!")
            break
        except TypeError:
            continue
    while True:
        try:
            user_age = int(input("Age: "))
            if user_age == 0:
                raise print("Age can not equal 0!")
            break
        except ValueError:
            print("Age must be digits")
    while True:
        try:
            user_number = int(input("numb"))
            if user_number >= 

    user_email = input("email")
    user = Contact(user_name, user_surname, user_age, user_number, user_email)
    contact = user.data()
    #lst.append(contact)
    print(contact)
    return contact

    #print(user.data())
    #save_to_file(user.data())
    # Работа с памятью
    #lst.append(user)
    #print("lst", lst)
    #us_list.append(user.data())
    #print(us_list)
    #menu()

# Готово, Работает
# Принимаем список со списками контактов и распаковываем его для вывода на экран пользователя
def show_book(lst):
    if len(lst) == 0:
        print("Addressbook is empty!")
        menu()
    for index, data in enumerate(lst, 1):
        name, surname, age, number, email = data
        print(f"{index}. Name: {name} Surname: {surname} Age: {age} Number: {number} E-mail: {email} ")


# Выводим для пользователя список контактов и предлагаем изменить его по нумерации
# TODO Добавить исключения и возможность изменений либо конректного параметра/ либо не по индексации
def change_info(lst, x):
    #show_book(lst)
    #x = int(input("Enter the index of contact to change it."))
    #del lst[x]
    print(lst[x])
    #name = input("New name")
    #surname = input("New surname")
    #age = input("New age")
    #number = input("New number")
    #email = input("New email")
    #new_data = [name, surname, age, number, email]
    lst[x] = create_user()
    print(lst)
    #return lst
    #оптимизированный вариант
    save_to_file(lst)
    menu()

    #Найти элемент и удалить

# TODO удаление элемента в списке подумать
def del_info(lst, x):
    del lst[x]
    save_to_file(lst)


def find_user(lst, phone=False, find_result=False):
    index = -1
    find_list = []
    index_list = []
    if phone:
        find_key_number = input("Enter a number or part of it to find contact: ")
        for i in lst:
            index += 1
            if find_key_number in i[-2]:
                print("Nashel!", i)
                find_list.append(i)
                index_list.append(index)
                print(index_list)
                find_result = True
    else:
        find_key_name = input("Enter the contact's Name")
        find_key_surname = input("Enter surname:")
        for i in lst:
            index += 1
            if find_key_name in i[0] or find_key_surname in i[1]:
                find_list.append(i)
                index_list.append(index)
                find_result = True
    if not find_result:
        print("There's no contact with that parameters!")
        menu()

    # if only 1 match
    if len(find_list) == 1:
        show_book(find_list)
        index = index_list[0]
    else:
        show_book(find_list)
        index = int(input("Choose the index of contact that you need: "))
        show_book([find_list[index - 1]])
        index = index_list[index-1]
    find(lst, index)


# TODO Поиск по адресной книге(либо имя\Фамилия или телефон)
def find(lst, index):
    while True:
        choice = input("1 - Edit contact\t2 - Delete contact\t 3 - Back to menu\n")
        if choice == '1':
            change_info(lst, index)
        elif choice == '2':
            del_info(lst, index)
        elif choice == '3':
            menu()


# Оптимизировать меню
def menu():
    action = input("1 - Add to Addressbook\n2 - Show contacts\n3 - Find Contact\n4 - Exit\n")
    if action == '1':
        user_list.append(create_user())
        save_to_file(user_list)
        menu()
    elif action == '2':
        show_book(user_list)
        input("Press any key to continue...")
        menu()
    elif action == '3':
        find_user(user_list, True)
        menu()
    elif action == '4':
        sys.exit()
    else:
        menu()

# user_list = [Список кортежей с параметрам контакт]
# Проверяем есть ли файл для записи(если нет - создаем и добавляем в него пустой список) иначе загружаем список с данными
if os.path.exists('Data.pickle'):
    user_list = load_from_file()
    print(user_list)
    menu()
else:
    with open('Data.pickle', 'wb') as f:
        pickle.dump([], f)
    user_list = load_from_file()
    menu()
"""
start = time.time()
# вызовите здесь функцию
end = time.time()
print(end-start)"""