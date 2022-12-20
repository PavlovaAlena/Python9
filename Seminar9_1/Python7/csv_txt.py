#******модуль экспорта между форматами csv и txt***************

def csv_to_txt():
    import csv
    with open("phone.txt", "w", encoding="utf-8") as output_file:
        with open("phone.csv", "r", encoding="utf-8") as input_file:
            [output_file.write(",".join(row)+"\n") for row in csv.reader(input_file)]
    output_file.close()

def txt_to_csv():
    import csv
    with open("phone.txt", "r", encoding="utf-8") as input_file:
        stripped = (line.strip() for line in input_file)
        lines = (line.split(",") for line in stripped if line)
        with open("phone.csv", "w", encoding="utf-8") as output_file:
            writer = csv.writer(output_file,lineterminator="\n")
            writer.writerows(lines)