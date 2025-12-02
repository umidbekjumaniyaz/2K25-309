from abc import ABC, abstractmethod
from modules.transport.vehicles import Bus, Taxi, Metro


class TransportFactory(ABC):
    @abstractmethod
    def create_vehicle(self, identifier):
        pass


class BusFactory(TransportFactory):
    def create_vehicle(self, route_number):
        return Bus(route_number)


class TaxiFactory(TransportFactory):
    def create_vehicle(self, car_id):
        return Taxi(car_id)


class MetroFactory(TransportFactory):
    def create_vehicle(self, line_name):
        return Metro(line_name)


class TransportCreator:
    _factories = {
        "bus": BusFactory(),
        "taxi": TaxiFactory(),
        "metro": MetroFactory()
    }
    
    @classmethod
    def create(cls, vehicle_type, identifier):
        factory = cls._factories.get(vehicle_type.lower())
        if factory:
            return factory.create_vehicle(identifier)
        raise ValueError(f"Noma'lum transport turi: {vehicle_type}")
