from abc import ABC, abstractmethod

class UnmannedVehicle(ABC):
    """ 
        An autonomous vehicle have to do his mission automatically.
        This mission can be configured by an operator.
    """
    @abstractmethod
    def moving(self):
        pass

class AerialVehicle(UnmannedVehicle):
    """ A vehicle made for aerial fields."""
    @abstractmethod
    def aerial_photo(self):
        pass

class GroundVehicle(UnmannedVehicle):
    """ A vehicle made for ground fields."""
    @abstractmethod
    def mapping(self):
        pass

class UnderseaVehicle(UnmannedVehicle):
    """ A vehicle made for undersea fields."""
    @abstractmethod
    def collecting_water(self):
        pass

class UAV(AerialVehicle):
    """Unmanned Aerial Vehicle"""
    def moving(self):
        print("I am flying")
        
    def aerial_photo(self):
        print("I am taking aerial photos")

class UUV(UnderseaVehicle):
    """Unmanned Undersea Vehicle"""
    def moving(self):
        print("I am diving")

    def collecting_water(self):
        print("I am collecting water samples")

class UGV(GroundVehicle):
    """Unmanned Ground Vehicle"""
    def moving(self):
        print("I am moving on the ground")

    def mapping(self):
        print("I am mapping the area")

if __name__ == "__main__" :

    uav = UAV()
    uav.moving()
    uav.aerial_photo()

    ugv = UGV()
    ugv.moving()
    ugv.mapping()

    uuv = UUV()
    uuv.moving()
    uuv.collecting_water()