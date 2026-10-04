"""
Factory: It is creational design pattern that provides a standardized interface for creating objects.
"""

class Truck:
    def __init__(self):
        self.type = "Road Logistics"
    
    def deliver(self):
        return "Delivering cargo by land in a truck"

class Ship:
    def __init__(self):
        self.type = "Sea Logistics"
    
    def deliver(self):
        return "Delivering cargo by water in ship"


# Build the factory using static method with staticmethod because it does not need to maintain any internal state or track instance variables to do its job.
# It's only responsibility is to take input and process it and return new object.
class LogisticsFactory:
    @staticmethod
    def get_transport(type: str):
        # Mapping of string to class
        transports = {
            "truck": Truck,
            "ship": Ship
        }

        choosen_class = transports.get(type.lower())
        if not choosen_class:
            raise ValueError(f"unknown transport type: {type}")
        return choosen_class()

transport_type = "ship"
delivery_vehicle = LogisticsFactory.get_transport(transport_type)

print(delivery_vehicle.type)
print(delivery_vehicle.deliver())