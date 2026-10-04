"""
Builder: It's creational design pattern, When an object constructor reuires more than 4 or 5 parameters, making it hard to track what positional arguments mean.
When you need to create different variations of the same object.
This pattern makes complex constructor/object initialisation simple.
This is to fix the monster constructor.
"""

class House:
    def __init__(self, bed, bath, kitchen, garden, pool, smart):
        self.bed = bed
        self.bath = bath
        self.kitchen = kitchen
        self.garden = garden
        self.pool = pool
        self.smart = smart
    
    def __str__(self):
        features = [f"Bed rooms: {self.bed}",
                    f"Bath rooms: {self.bath}",
                    f"Kitchen rooms: {'Yes' if self.kitchen else 'No'}",
                    f"Gardens: {'Yes' if self.garden else 'No'}",
                    f"Pool: {'Yes' if self.pool else 'No'}",
                    f"Smart Home: {'Yes' if self.smart else 'No'}"]
        return " | ".join(features)

# Builder Pattern
class HouseBuilder:
    def __init__(self):
        self.bed = 1
        self.bath = 1
        self.kitchen = True
        self.garden = False
        self.pool = False
        self.smart = False
    
    def set_bed(self, nos):
        self.bed = nos
        return self
    
    def set_bath(self, nos):
        self.bath = nos
        return self
    
    def set_kitchen(self):
        self.kithen = True
        return self
    
    def set_garden(self):
        self.garden = True
        return self
    
    def set_pool(self):
        self.pool = True
        return self
    
    def set_smart(self):
        self.smart = True
        return self
    
    def build_home(self):
        return House(self.bed,
                    self.bath,
                    self.kitchen,
                    self.garden,
                    self.pool,
                    self.smart)

# Create a custom house
house_builder = HouseBuilder()

custom_house = (house_builder.set_bed(4)
    .set_bath(3)
    .set_garden()
    .set_kitchen()
    .set_pool()
    .set_smart()
    .build_home())
print(f"Custom house is: {custom_house}")