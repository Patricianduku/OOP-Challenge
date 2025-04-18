class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5    
        self.energy = 5   
        self.happiness = 5 
        self.tricks = []  

    def eat(self):
        self.hunger = max(0, self.hunger - 3)  
        self.happiness = min(10, self.happiness + 1)  
        print(f"{self.name} chewed on some bones! Yum! 😋")

    def sleep(self):  
        self.energy = min(10, self.energy + 5)  
        print(f"Zzz... {self.name} is refreshed!")

    def play(self):
        self.energy = max(0, self.energy - 2)  
        self.happiness = min(10, self.happiness + 2)  
        self.hunger = min(10, self.hunger + 1)  
        print(f"{self.name} had fun playing outside with other pets! 🐾")

    def train(self, trick):
        if trick not in self.tricks:
            self.tricks.append(trick)
            print(f"{self.name} learned {trick}! Way to go! 🏆")
        else:
            print(f"{self.name} knows it {trick}!")

    def show_tricks(self):
        if self.tricks:
            print(f"{self.name}'s tricks: {', '.join(self.tricks)}")
        else:
            print(f"{self.name} trying to improve in new tricks!")

    def get_status(self):
        print(f"\n{self.name}'s Status:")
        print(f"Hunger: {self.hunger}/10")
        print(f"Energy: {self.energy}/10")
        print(f"Happiness: {self.happiness}/10")



