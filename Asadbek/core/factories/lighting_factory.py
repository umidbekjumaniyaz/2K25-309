from abc import ABC, abstractmethod
from modules.lighting.lights import StreetLight, TrafficLight, ParkLight


class LightFactory(ABC):
    @abstractmethod
    def create_light(self, location):
        pass


class StreetLightFactory(LightFactory):
    def create_light(self, location):
        return StreetLight(location)


class TrafficLightFactory(LightFactory):
    def create_light(self, intersection):
        return TrafficLight(intersection)


class ParkLightFactory(LightFactory):
    def create_light(self, park_name):
        return ParkLight(park_name)


class LightingCreator:
    _factories = {
        "street": StreetLightFactory(),
        "traffic": TrafficLightFactory(),
        "park": ParkLightFactory()
    }
    
    @classmethod
    def create(cls, light_type, location):
        factory = cls._factories.get(light_type.lower())
        if factory:
            return factory.create_light(location)
        raise ValueError(f"Noma'lum chiroq turi: {light_type}")
