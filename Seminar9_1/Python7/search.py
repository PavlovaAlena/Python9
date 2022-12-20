#******модуль поиска контакта***************

def searchData(word, data):
    lstitem = []
    if len(data) > 0:
        for item in data:
            if word in item:
                lstitem.append(item)
    return lstitem