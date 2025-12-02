from core.singleton.config_manager import ConfigManager
from core.builders.zone_builder import ZoneBuilder
from core.adapters.weather_adapter import WeatherAdapter
from core.proxy.security_proxy import SecurityProxy


class SmartCityController:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance
    
    def __init__(self):
        if self._initialized:
            return
        self._initialized = True
        self._config = ConfigManager()
        self._zones = {}
        self._weather = WeatherAdapter()
        self._security = SecurityProxy()
        self._setup_default_zones()
    
    def _setup_default_zones(self):
        downtown = (ZoneBuilder("Markaz")
            .add_bus(1)
            .add_bus(5)
            .add_taxi("T001")
            .add_metro("Qizil")
            .add_street_light("Amir Temur ko'chasi")
            .add_traffic_light("Markaziy choraha")
            .add_camera("Hokimiyat binosi")
            .add_motion_sensor("Bank hududi")
            .add_solar_panel(1, 100)
            .build())
        
        residential = (ZoneBuilder("Turar-joy")
            .add_bus(12)
            .add_taxi("T002")
            .add_street_light("Tinchlik ko'chasi")
            .add_park_light("Bolalar bog'i")
            .add_camera("Kirish joyi")
            .add_alarm("1-uy")
            .add_wind_turbine(1, 50)
            .build())
        
        industrial = (ZoneBuilder("Sanoat")
            .add_bus(25)
            .add_street_light("Zavod ko'chasi")
            .add_traffic_light("Yuk mashinalar kirishi")
            .add_camera("Omborxona")
            .add_motion_sensor("Perimetr")
            .add_alarm("Bosh bino")
            .add_solar_panel(2, 200)
            .add_solar_panel(3, 200)
            .add_wind_turbine(2, 100)
            .build())
        
        self._zones["markaz"] = downtown
        self._zones["turar-joy"] = residential
        self._zones["sanoat"] = industrial
    
    def get_zone(self, zone_name):
        return self._zones.get(zone_name.lower())
    
    def get_all_zones(self):
        return list(self._zones.keys())
    
    def get_config(self):
        return self._config
    
    def get_weather(self):
        return self._weather
    
    def get_security(self):
        return self._security
    
    def get_system_status(self):
        total_vehicles = sum(len(z.vehicles) for z in self._zones.values())
        total_lights = sum(len(z.lights) for z in self._zones.values())
        total_sensors = sum(len(z.sensors) for z in self._zones.values())
        total_power = sum(len(z.power_sources) for z in self._zones.values())
        
        return {
            "city_name": self._config.get("city_name"),
            "zones": len(self._zones),
            "total_vehicles": total_vehicles,
            "total_lights": total_lights,
            "total_sensors": total_sensors,
            "total_power_sources": total_power
        }
    
    def activate_zone_lights(self, zone_name):
        zone = self.get_zone(zone_name)
        if not zone:
            return f"Zona topilmadi: {zone_name}"
        results = []
        for light in zone.lights:
            results.append(light.turn_on())
        return results
    
    def deactivate_zone_lights(self, zone_name):
        zone = self.get_zone(zone_name)
        if not zone:
            return f"Zona topilmadi: {zone_name}"
        results = []
        for light in zone.lights:
            results.append(light.turn_off())
        return results
    
    def activate_zone_security(self, zone_name):
        zone = self.get_zone(zone_name)
        if not zone:
            return f"Zona topilmadi: {zone_name}"
        results = []
        for sensor in zone.sensors:
            results.append(sensor.activate())
        return results
    
    def start_zone_power(self, zone_name):
        zone = self.get_zone(zone_name)
        if not zone:
            return f"Zona topilmadi: {zone_name}"
        results = []
        for source in zone.power_sources:
            results.append(source.generate())
        return results
    
    def get_zone_transport_status(self, zone_name):
        zone = self.get_zone(zone_name)
        if not zone:
            return f"Zona topilmadi: {zone_name}"
        return [v.get_status() for v in zone.vehicles]
