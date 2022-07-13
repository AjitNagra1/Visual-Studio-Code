class Patient:
    def __init__(self, name, sugar, fat, salt):
        self.name = name
        self.sugar = sugar
        self.fat = fat
        self.salt = salt
    
    def diagnosis(self):
        if (self.sugar<=37.5) and (self.fat<=77) and (self.salt<=2300):
            print(f"{self.name} is healthy")
        else:
            print(f"{self.name} is unhealthy")

P1=Patient(input("Enter your name: "),int(input("Enter your sugar intake: ")),
int(input("Enter your fat intake: ")),int(input("Enter your salt intake: ")))

P2=Patient(input("Enter your name: "),int(input("Enter your sugar intake: ")),
int(input("Enter your fat intake: ")),int(input("Enter your salt intake: ")))

P3=Patient(input("Enter your name: "),int(input("Enter your sugar intake: ")),
int(input("Enter your fat intake: ")),int(input("Enter your salt intake: ")))

P1.diagnosis()
P2.diagnosis()
P3.diagnosis()

