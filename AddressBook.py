# TODO Создайте собственную программу, работающая из командной строки и
#  позволяющую просматривать, добавлять, изменять, удалять или искать контактные данные ваших знакомых.
#  Кроме этого информация должна сохроняться на диске для последующего пользования
import os.path
import pickle
import sys


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


def str_check(name):
    while True:
        try:
            string = input(f"{name}: ").capitalize()
            for i in string:
                if not i.isalpha():
                    raise ValueError(f"{name} must contain only letters!")
            break
        except TypeError:
            continue
    return string

# TODO digit didn't convert to string
def digit_check(name, age_check=False):
    while True:
        try:
            digit = int(input(f"{name}: "))
            if age_check:
                if digit == 0 or digit > 100:
                    raise print("Age cannot equals 0 or bigger 100!")
                break
            else:
                if len(str(digit)) > 15:
                    raise print("Phone number must consist less than 14 digits!")
                digit = str(digit)
                print(digit)
                break
        except ValueError:
            continue
    return digit


# Создаем контакт и возвращаем список с данными
def create_user():
    user_name = str_check('Name')
    user_surname = str_check('Surname')
    user_age = digit_check('Age', True)
    user_number = digit_check("Phone number")
    user_email = input("E-mail: ")
    user = Contact(user_name, user_surname, user_age, user_number, user_email)
    contact = user.data()
    return contact


# Принимаем список со списками контактов и распаковываем его для вывода на экран пользователя
def show_book(data_list):
    if len(data_list) == 0:
        print("Addressbook is empty!")
        menu()
    for index, data in enumerate(data_list, 1):
        name, surname, age, number, email = data
        print(f"{index}. Name: {name} Surname: {surname} Age: {age} Number: {number} E-mail: {email} ")


def change_info(data_list, index):
    data_list[index] = create_user()
    save_to_file(data_list)
    menu()


def del_info(data_list, index):
    del data_list[index]
    save_to_file(data_list)


# find user by name/phone-number and interact it
def find_user(data_list, find_by_phone=False, find_result=False):
    index = -1
    find_list = []
    index_list = []
    if find_by_phone:
        find_key_number = digit_check("Enter the phone number or part of it to find contact")
        print(str(find_key_number))
        for i in data_list:
            index += 1
            if find_key_number in i[-2]:
                find_list.append(i)
                index_list.append(index)
                find_result = True
    else:
        find_key_name = str_check("Enter Name")
        find_key_surname = str_check("Enter Surname")
        for i in data_list:
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
        while True:
            try:
                index = int(input("Choose the index of contact: "))
                if index <= 0:
                    continue
                show_book([find_list[index - 1]])
                index = index_list[index-1]
                break
            except IndexError:
                continue
    find(data_list, index)


# TODO Поиск по адресной книге(либо имя\Фамилия или телефон)
def find(data_list, index):
    while True:
        choice = input("1 - Edit contact\t2 - Delete contact\t 3 - Back to menu\n")
        if choice == '1':
            change_info(data_list, index)
        elif choice == '2':
            del_info(data_list, index)
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
        while True:
            find_by = input("Find contact by:\n1 - Phone number\n2 - Name and Surname\n")
            if find_by == '1':
                find_user(user_list, True)
                break
            elif find_by == '2':
                find_user(user_list)
                break
            else:
                print("Please, choose the option!")
                continue
        menu()
    elif action == '4':
        sys.exit()
    else:
        menu()


# Проверяем есть ли файл для записи(если нет - создаем и добавляем в него пустой список)
# иначе загружаем список с данными
if os.path.exists('Data.pickle'):
    user_list = load_from_file()
    menu()
else:
    with open('Data.pickle', 'wb') as f:
        pickle.dump([], f)
    user_list = load_from_file()
    menu()
