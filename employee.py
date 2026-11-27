from datetime import datetime

class Employee:
    def __init__(self, id, name, surname, position, salary):
        self.id = id
        self.name = name
        self.surname = surname
        self.position = position
        self.start_date = datetime.now()
        self.salary = salary

    def full_name(self):
        for i in employees:
            print(i)
            break


employees = []


employees.append(Employee(34254, 'Anna', 'Henrihsone', 'Finanšu direktore', 4200 ))
employees.append(Employee(45243, 'Oskars', 'Bērziņš', 'CTO', 5000))
employees.append(Employee(64523, 'Ilze', 'Andersone', 'Programmētāja', 3100))


for e in employees:
    print(f"{e.name} ({e.position}) - Start date: {e.start_date}")

