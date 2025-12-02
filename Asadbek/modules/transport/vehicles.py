from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def move(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass
    
    @abstractmethod
    def get_status(self):
        pass


class Bus(Vehicle):
    def __init__(self, route_number):
        self.route_number = route_number
        self.is_moving = False
        self.passengers = 0
    
    def move(self):
        self.is_moving = True
        return f"Avtobus #{self.route_number} harakatda"
    
    def stop(self):
        self.is_moving = False
        return f"Avtobus #{self.route_number} to'xtadi"
    
    def get_status(self):
        status = "harakatda" if self.is_moving else "to'xtagan"
        return f"Avtobus #{self.route_number}: {status}, yo'lovchilar: {self.passengers}"
    
    def board_passengers(self, count):
        self.passengers += count


class Taxi(Vehicle):
    def __init__(self, car_id):
        self.car_id = car_id
        self.is_moving = False
        self.is_available = True
    
    def move(self):
        self.is_moving = True
        self.is_available = False
        return f"Taksi #{self.car_id} yo'lda"
    
    def stop(self):
        self.is_moving = False
        return f"Taksi #{self.car_id} to'xtadi"
    
    def get_status(self):
        if self.is_available:
            return f"Taksi #{self.car_id}: bo'sh"
        status = "yo'lda" if self.is_moving else "kutmoqda"
        return f"Taksi #{self.car_id}: {status}"
    
    def complete_trip(self):
        self.is_available = True
        self.is_moving = False


class Metro(Vehicle):
    def __init__(self, line_name):
        self.line_name = line_name
        self.is_moving = False
        self.current_station = "Depot"
    
    def move(self):
        self.is_moving = True
        return f"Metro {self.line_name} liniyasi harakatda"
    
    def stop(self):
        self.is_moving = False
        return f"Metro {self.line_name} bekatlarda to'xtadi"
    
    def get_status(self):
        status = "harakatda" if self.is_moving else "bekatda"
        return f"Metro {self.line_name}: {status}, joriy bekat: {self.current_station}"
    
    def arrive_at_station(self, station):
        self.current_station = station
        self.is_moving = False
