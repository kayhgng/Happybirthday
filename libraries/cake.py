# cake.py
#Alikay_h
#KayH GNG

class Cake:
    def __init__(self, flavor="chocolate", candles=1):
        self.flavor = flavor
        self.candles = candles
        self.eaten = False
    
    def light_candles(self):
        if self.candles > 0:
            print(f"🔥 Lighting {self.candles} candles on the {self.flavor} cake!")
        else:
            print("No candles to light!")

    def blow_candles(self):
        if self.candles > 0:
            print("🎂 Whooosh! Candles blown out! Make a wish! ✨")
            self.candles = 0
        else:
            print("There are no candles left to blow out!")

    def eat(self):
        if not self.eaten:
            print(f"🍰 Eating the delicious {self.flavor} cake... Yummy!")
            self.eaten = True
        else:
            print("The cake is already eaten! No crumbs left! 😢")
