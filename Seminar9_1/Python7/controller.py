from csv_txt import *
from writing import writingFile
# from read import readFile
from read import *
from output import displayScreen
from search import searchData

# *********************


def inputEntry():
    entry = []
    lastName = input("Введите фамилию: ")
    entry.append(lastName)
    firstName = input("Введите имя: ")
    entry.append(firstName)
    phoneNumber = input("Введите номер контакта: ")
    entry.append(phoneNumber)
    note = input("Введите описание: ")
    entry.append(note)
    return entry

# *********************


def greeting():
    print("Перед Вами телефонная книга.")

# *********************


def choice():
    print("Доступные операции с книгой:\n\
    1 - добавить запись в книгу;\n\
    2 - вывести всю книгу;\n\
    3 - поиск контакта;\n\
    4 - экспортировать книгу csv в txt;\n\
    5 - экспортировать книгу txt в csv;\n\
    6 - выход из книги.")
    ch = input("Выберите действие: ")
    if ch == "1":
        writingFile(inputEntry())
        print("Данные внесены в справочник")
    elif ch == "2":
        readFilePnd()
        # data = readFile()
        # displayScreen(data)
    elif ch == "3":
        word = input("Введите данные для поиска: ")
        data = readFile()
        lstitem = searchData(word, data)
        displayScreen(lstitem, "Данные не обнаружены")
    elif ch == "4":
        csv_to_txt()
        print("Файл phone.csv экспортирован в phone.txt")
    elif ch == "5":
        txt_to_csv()
        print("Файл phone.txt экспортирован в phone.csv")
    else:
        print("Всего хорошего!")
        exit()

    if ch != "6":
        choice()
