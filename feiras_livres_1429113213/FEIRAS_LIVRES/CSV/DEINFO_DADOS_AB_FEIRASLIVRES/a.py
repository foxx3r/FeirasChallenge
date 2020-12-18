import csv

with open("test.csv", "r") as f:
    csv_reader = csv.reader(f, delimiter=",")
    for row in csv_reader:
        print(f"""
nome: {row[0]}
idade: {row[1]}
sexo: {row[2]}
ideologia: {row[3]}
religião: {row[4]}""")
