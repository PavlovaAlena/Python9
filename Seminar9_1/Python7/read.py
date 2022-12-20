# ******модуль чтения из файла***************

def readFilePnd():
    import pandas
    data = pandas.read_csv('phone.csv')
    print(data)
    return data


def readFile():
    with open("phone.csv", "r",  encoding="utf-8") as file:
        data = []
        t = []
        for line in file:
            if "," in line:
                temp = line.strip().split(",")
                data.append(temp)
            elif ";" in line:
                temp = line.strip().split(";")
                data.append(temp)
            elif ":" in line:
                temp = line.strip().split(":")
                data.append(temp)
            elif line != "":
                if line != "\n":
                    t.append(line.strip())
                else:
                    data.append(t)
                    t = []
    return data
