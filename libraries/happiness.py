# happiness.py
#Alikay_h
#KayhGNG

class Happiness:
    def __init__(self):
        self.level = 0
    
    def increase(self, amount):
        self.level += amount
        if self.level > 100:
            self.level = 100
        print(f"Happy level increased! Current level: {self.level}")
    
    def decrease(self, amount):
        self.level -= amount
        if self.level < 0:
            self.level = 0
        print(f"Happy level decreased. Current level: {self.level}")
    
    def is_happy(self):
        return self.level >= 80

