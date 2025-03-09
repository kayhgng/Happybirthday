# party.py
#KayHGNG
#Alikay_h

class Party:
    def __init__(self, music="pop", lights="flashing"):
        self.music = music
        self.lights = lights
        self.dancing = False
    
    def start(self, dance=False, music=None):
        if music:
            self.music = music
        print(f"🎶 Playing {self.music} music... 🎶")
        self.turn_on_lights()
        if dance:
            self.start_dancing()

    def turn_on_lights(self):
        print(f"💡 Lights are {self.lights}... Let the party begin!")

    def start_dancing(self):
        self.dancing = True
        print("💃 Let's dance! 🕺 The party is on!")

    def stop_party(self):
        self.dancing = False
        print("🛑 Party is over... Let's clean up!")
        self.turn_off_lights()

    def turn_off_lights(self):
        print("💡 Lights off... Party is winding down.")
