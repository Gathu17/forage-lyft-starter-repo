from abc import ABC
from car import Car

class Octoprime(Car,ABC):
    def __init__(self,tires_array):
        self.tires_array = tires_array
    
    def needs_service(self):
        sum = 0
        for x in self.tires_array:
            sum += x                       

        if sum < 3:
          return False
        else:
          return True