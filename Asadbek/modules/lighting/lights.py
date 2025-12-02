from abc import ABC, abstractmethod


class Light(ABC):
    @abstractmethod
    def turn_on(self):
        pass
    
    @abstractmethod
    def turn_off(self):
        pass
    
    @abstractmethod
    def get_status(self):
        pass


class StreetLight(Light):
    def __init__(self, location):
        self.location = location
        self.is_on = False
        self.brightness = 100
    
    def turn_on(self):
        self.is_on = True
        return f"Ko'cha chirog'i ({self.location}) yoqildi"
    
    def turn_off(self):
        self.is_on = False
        return f"Ko'cha chirog'i ({self.location}) o'chirildi"
    
    def get_status(self):
        status = "yoniq" if self.is_on else "o'chiq"
        return f"Ko'cha chirog'i ({self.location}): {status}, yorqinlik: {self.brightness}%"
    
    def set_brightness(self, level):
        self.brightness = max(0, min(100, level))


class TrafficLight(Light):
    def __init__(self, intersection):
        self.intersection = intersection
        self.is_on = False
        self.current_color = "red"
    
    def turn_on(self):
        self.is_on = True
        return f"Svetofor ({self.intersection}) yoqildi"
    
    def turn_off(self):
        self.is_on = False
        return f"Svetofor ({self.intersection}) o'chirildi"
    
    def get_status(self):
        if not self.is_on:
            return f"Svetofor ({self.intersection}): o'chiq"
        return f"Svetofor ({self.intersection}): {self.current_color}"
    
    def change_color(self, color):
        if color in ["red", "yellow", "green"]:
            self.current_color = color


class ParkLight(Light):
    def __init__(self, park_name):
        self.park_name = park_name
        self.is_on = False
        self.mode = "normal"
    
    def turn_on(self):
        self.is_on = True
        return f"Park chirog'i ({self.park_name}) yoqildi"
    
    def turn_off(self):
        self.is_on = False
        return f"Park chirog'i ({self.park_name}) o'chirildi"
    
    def get_status(self):
        status = "yoniq" if self.is_on else "o'chiq"
        return f"Park chirog'i ({self.park_name}): {status}, rejim: {self.mode}"
    
    def set_mode(self, mode):
        self.mode = mode
