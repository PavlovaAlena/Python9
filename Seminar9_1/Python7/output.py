#******модуль вывода контакта(ов) на экран***************

def displayScreen(data, txt="Справочник пуст!"):
    if len(data) > 0:
        print("Фамилия".center(20), "Имя".center(20), "Телефон".center(20), "Описание".center(20))
        print("-"*130)
        for item in data:
            print(item[0].center(20), item[1].center(20), item[2].center(20), item[3].center(20))
    else:
        print(txt)