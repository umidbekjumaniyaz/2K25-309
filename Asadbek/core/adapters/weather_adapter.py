from abc import ABC, abstractmethod


class ExternalWeatherAPI:
    def fetch_data(self):
        return {
            "temp_fahrenheit": 68,
            "wind_mph": 12,
            "humidity_percent": 65,
            "conditions": "partly_cloudy"
        }


class WeatherInterface(ABC):
    @abstractmethod
    def get_temperature(self):
        pass
    
    @abstractmethod
    def get_wind_speed(self):
        pass
    
    @abstractmethod
    def get_humidity(self):
        pass
    
    @abstractmethod
    def get_conditions(self):
        pass


class WeatherAdapter(WeatherInterface):
    def __init__(self):
        self._api = ExternalWeatherAPI()
        self._data = None
    
    def _fetch_if_needed(self):
        if self._data is None:
            self._data = self._api.fetch_data()
    
    def get_temperature(self):
        self._fetch_if_needed()
        fahrenheit = self._data["temp_fahrenheit"]
        celsius = (fahrenheit - 32) * 5 / 9
        return round(celsius, 1)
    
    def get_wind_speed(self):
        self._fetch_if_needed()
        mph = self._data["wind_mph"]
        kmh = mph * 1.60934
        return round(kmh, 1)
    
    def get_humidity(self):
        self._fetch_if_needed()
        return self._data["humidity_percent"]
    
    def get_conditions(self):
        self._fetch_if_needed()
        conditions_map = {
            "sunny": "quyoshli",
            "partly_cloudy": "qisman bulutli",
            "cloudy": "bulutli",
            "rainy": "yomg'irli",
            "snowy": "qorli"
        }
        return conditions_map.get(self._data["conditions"], self._data["conditions"])
    
    def get_full_report(self):
        return (
            f"Ob-havo: {self.get_conditions()}\n"
            f"Harorat: {self.get_temperature()}°C\n"
            f"Shamol: {self.get_wind_speed()} km/s\n"
            f"Namlik: {self.get_humidity()}%"
        )
    
    def refresh(self):
        self._data = None
