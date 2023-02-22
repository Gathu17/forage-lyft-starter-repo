from abc import ABC
from car import Car



class SpindlerBattery(Car,ABC):
    def __init__(self,last_service_date,current_date):
      super().__init__(last_service_date)
      self.current_date = current_date
      self.last_service_date = last_service_date
    def needs_service(self):
      date_to_be_serviced = self.last_service_date.replace(year = self.last_service_date.year + 2)
      if date_to_be_serviced < self.current_date:
        return True
      else:
        return False