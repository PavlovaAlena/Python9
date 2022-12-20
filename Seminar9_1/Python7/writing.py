##******модуль записи новых данных в файл***************

def writingFile(data):
    import csv
    with open("phone.csv", "a", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile, lineterminator="\r")
        writer.writerow(data)