from datetime import datetime

class employee:
    def __init__(self, id, name, surname, position):
        self.id = id
        self.name = name
        self.surname = surname
        self.position = position
        self.start_date = datetime.now()

employee = []

employee.append = employee(34254, "Anna", "Henrihsone", "Finanšu direktore")
employee.append = employee(34254, "Oskars", "Reins", "Marketinga direktors")


for e in employee:
    print(f"{e.id} {e.name} {e.surname} {e.position} - Start date: {