import csv

employees = [["Name", "Age", "Job"],
             ["SpongeBob", 30, "Cook"],
             ["Patrick ", 37, "Unemployed"],
             ["Sandy", 27, "Scientist"]]

filePath = 'Files/prueba2.csv'

with open(filePath, "w") as file:
    writer = csv.writer(file)
    for employee in employees:
        writer.writerow(employee)
    print("Archive created succesfully!")