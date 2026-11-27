class Dog:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"Cau mani sauc {self.name}!")

    def walk(self, steps):
        print (f"{self.name} nostaigāja {steps} solus.")



dog_1 = Dog("Reksis")
dog_2 = Dog("Luna")

dog_1.introduce()
dog_1.walk(10)