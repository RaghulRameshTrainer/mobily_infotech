from abc import ABC , abstractmethod
class Car(ABC):
    @abstractmethod
    def breaks(self):
        pass
    @abstractmethod
    def seats(self):
        pass
    @abstractmethod
    def engine(self):
        pass
    @abstractmethod
    def door(self):
        pass
    @abstractmethod
    def tires(self):
        pass

class EcoSport(Car):
    def __init__(self,model):
        self.model=model
    def breaks(self):
        self.break_status="Application"
    def seats(self):
        self.seats_status='Fitted'
    def engine(self):
        self.type='Powerstrain'
    def door(self):
        self.count=4
    def tires(self):
        self.tire_count=6

    def get_price(self,car_model):
        if car_model=='EcoSport':
            print(1700000)
        elif car_model=='Figo':
            print(1200000)
        else:
            print('Please check at showrooms')
c1=EcoSport('2022')
c1.get_price('Endeavour')