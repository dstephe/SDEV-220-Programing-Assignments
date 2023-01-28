
#Super Class for Vehicles
class Vehicle():
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

#Subclass of Vehicles for Automobiles
class Automobile(Vehicle):
    def __init__(self,vehicle_type,year,make,model,doors,roof):
        super().__init__(vehicle_type)#gets the vehicle_type from Vehicles
        self.year=year
        self.make=make
        self.model=model
        self.doors=doors
        self.roof=roof

#assigns object for Automobile
user_vehicle=Automobile('Vehicle Type: Car','Year(Ex:2001):','Make(Ex:Toyota):','Model(Camry):','# of doors:','Type of roof(Ex:Normal, Sunroof, Moonroof, Convertible, etc):')

#function for accepted user input for the vehicle
def car_input():
    
    user_vehicle.vehicle_type='\nVehicle Type: Car'#Vehicle Type is Car for this exercise

    print("Please enter the following info about your car.")

    print("Year(Ex:2001):")
    user_vehicle.year=input()

    print("Make(Ex:Toyota):")
    user_vehicle.make=input()

    print("Model(Camry):")
    user_vehicle.model=input()

    print("# of doors(2 or 4):")
    user_vehicle.doors=input()

    print("Type of roof(Solid, Sunroof, or Convertible):")
    user_vehicle.roof=input()

#prints out list of car info
def car_list():
    print(user_vehicle.vehicle_type)

    print("Year:",user_vehicle.year)

    print("Make:",user_vehicle.make)

    print("Model:", user_vehicle.model)

    print("Number of doors:", user_vehicle.doors)

    print("Type of roof:", user_vehicle.roof)

#calls the two functions
car_input()
car_list()
