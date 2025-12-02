from core.factories.transport_factory import TransportCreator
from core.factories.lighting_factory import LightingCreator
from modules.security.sensors import MotionSensor, Camera, AlarmSystem
from modules.energy.power_systems import SolarPanel, WindTurbine


class CityZone:
    def __init__(self, name):
        self.name = name
        self.vehicles = []
        self.lights = []
        self.sensors = []
        self.power_sources = []
    
    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)
    
    def add_light(self, light):
        self.lights.append(light)
    
    def add_sensor(self, sensor):
        self.sensors.append(sensor)
    
    def add_power_source(self, source):
        self.power_sources.append(source)
    
    def get_info(self):
        info = [f"\n=== {self.name} zonasi ==="]
        info.append(f"Transportlar: {len(self.vehicles)}")
        info.append(f"Chiroqlar: {len(self.lights)}")
        info.append(f"Sensorlar: {len(self.sensors)}")
        info.append(f"Energiya manbalari: {len(self.power_sources)}")
        return "\n".join(info)


class ZoneBuilder:
    def __init__(self, zone_name):
        self._zone = CityZone(zone_name)
    
    def add_bus(self, route_number):
        vehicle = TransportCreator.create("bus", route_number)
        self._zone.add_vehicle(vehicle)
        return self
    
    def add_taxi(self, car_id):
        vehicle = TransportCreator.create("taxi", car_id)
        self._zone.add_vehicle(vehicle)
        return self
    
    def add_metro(self, line_name):
        vehicle = TransportCreator.create("metro", line_name)
        self._zone.add_vehicle(vehicle)
        return self
    
    def add_street_light(self, location):
        light = LightingCreator.create("street", location)
        self._zone.add_light(light)
        return self
    
    def add_traffic_light(self, intersection):
        light = LightingCreator.create("traffic", intersection)
        self._zone.add_light(light)
        return self
    
    def add_park_light(self, park_name):
        light = LightingCreator.create("park", park_name)
        self._zone.add_light(light)
        return self
    
    def add_motion_sensor(self, area):
        sensor = MotionSensor(area)
        self._zone.add_sensor(sensor)
        return self
    
    def add_camera(self, location):
        sensor = Camera(location)
        self._zone.add_sensor(sensor)
        return self
    
    def add_alarm(self, building):
        sensor = AlarmSystem(building)
        self._zone.add_sensor(sensor)
        return self
    
    def add_solar_panel(self, panel_id, capacity):
        source = SolarPanel(panel_id, capacity)
        self._zone.add_power_source(source)
        return self
    
    def add_wind_turbine(self, turbine_id, capacity):
        source = WindTurbine(turbine_id, capacity)
        self._zone.add_power_source(source)
        return self
    
    def build(self):
        return self._zone
