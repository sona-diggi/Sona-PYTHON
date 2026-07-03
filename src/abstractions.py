from abc import abstractmethod, ABC

class vehicle(ABC):
    def name(self):
        print("hello")
    
    @abstractmethod
    def wheels(self):
        pass

    @abstractmethod
    def keys(self):
        pass

class car(vehicle):
    def wheels(self):
        print("car1 4 wheel")

    


v=car()
v.wheels()