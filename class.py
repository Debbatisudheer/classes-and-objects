class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start_engine(self):
        print(f"The {self.brand} {self.model}'s engine is now running.")

# Create a Car class that inherits from the Vehicle class
class Car(Vehicle):
    def __init__(self, brand, model, year, fuel_type, num_doors):
        super().__init__(brand, model, year)
        self.fuel_type = fuel_type
        self.num_doors = num_doors

    def drive(self):
        print(f"The {self.brand} {self.model} is now driving on {self.fuel_type}.It has {self.num_doors} doors.")

# Create a Bike class that inherits from the Vehicle class
class Bike(Vehicle):
    def __init__(self, brand, model, year, bike_type, color):
        super().__init__(brand, model, year)
        self.bike_type = bike_type
        self.color = color

    def ride(self):
        print(f"The {self.brand} {self.model} is now riding. Type: {self.bike_type}. Color: {self.color}.")

# Create a Cycle class that inherits from the Vehicle class
class Cycle(Vehicle):
    def __init__(self, brand, model, year, num_wheels, has_basket):
        super().__init__(brand, model, year)
        self.num_wheels = num_wheels
        self.has_basket = has_basket

    def pedal(self):
        print(f"The {self.brand} {self.model} is now pedaling with {self.num_wheels} wheels.Has basket: {self.has_basket}.")

# Create a Tractor class that inherits from the Vehicle class
class Tractor(Vehicle):
    def __init__(self, brand, model, year, hitch_type, num_plows):
        super().__init__(brand, model, year)
        self.hitch_type = hitch_type
        self.num_plows = num_plows

    def plow_field(self):
        print(f"The {self.brand} {self.model} is now plowing the field. Hitch type: {self.hitch_type}. Number of plows: {self.num_plows}.")

# Creating instances of the Car, Bike, Cycle, and Tractor classes
car = Car(brand="Toyota", model="Camry", year=2022, fuel_type="Petrol", num_doors=4)
bike = Bike(brand="Harley-Davidson", model="Street 750", year=2023, bike_type="Cruiser", color="Black")
cycle = Cycle(brand="Schwinn", model="Classic", year=2024, num_wheels=2, has_basket=True)
tractor = Tractor(brand="John Deere", model="1234", year=2025, hitch_type="Three-Point Hitch", num_plows=5)

# Accessing attributes and calling methods for each vehicle
print(f"Car - Brand: {car.brand}, Model: {car.model}, Year: {car.year}, Fuel Type: {car.fuel_type}, Doors: {car.num_doors}")
car.start_engine()
car.drive()

print(f"\nBike - Brand: {bike.brand}, Model: {bike.model}, Year: {bike.year}, Bike Type: {bike.bike_type}, Color: {bike.color}")
bike.start_engine()
bike.ride()

print(f"\nCycle - Brand: {cycle.brand}, Model: {cycle.model}, Year: {cycle.year}, Wheels: {cycle.num_wheels}, Has Basket: {cycle.has_basket}")
cycle.start_engine()
cycle.pedal()

print(f"\nTractor - Brand: {tractor.brand}, Model: {tractor.model}, Year: {tractor.year}, Hitch Type: {tractor.hitch_type}, Plows: {tractor.num_plows}")
tractor.start_engine()
tractor.plow_field()