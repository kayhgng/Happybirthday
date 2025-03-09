# Happy Birthday Program v1.0
import happiness
import cake
import party

def celebrate_birthday(friend):
    print(f"🎉 Happy Birthday, {friend}! 🎉")
    
# Alikay_h
  #KayHGNG
    happiness.happiness.increase(50)
    

    birthday_cake = cake.Cake(flavor="chocolate", candles=3)
    birthday_cake.eat()
    

    birthday_party = party.Party(music="Happy Tune", lights="flashing")
    birthday_party.start(dance=True)
    
    while True:
        print("Wishing you endless success and bug-free code! 🚀")
        if happiness.happiness.is_happy():
            print("The friend is happy! 🎉")
            break

celebrate_birthday("My Coder Friend")
