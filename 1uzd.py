class employee:

    def __init__(self, name, surname):

        self.name = name
        self.surname = surname


    def full_name(self):
        print(f"sveiks mans vaārds ir{name}, un uzvārds {surname}.")


anna = employee("Anna", "Henrihsone")
oskars = employee("Oskars", "Reins")

anna.full_name()