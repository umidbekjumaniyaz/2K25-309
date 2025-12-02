from abc import ABC, abstractmethod


class PowerSource(ABC):
    @abstractmethod
    def generate(self):
        pass
    
    @abstractmethod
    def get_output(self):
        pass
    
    @abstractmethod
    def get_status(self):
        pass


class SolarPanel(PowerSource):
    def __init__(self, panel_id, capacity):
        self.panel_id = panel_id
        self.capacity = capacity
        self.is_generating = False
        self.current_output = 0
    
    def generate(self):
        self.is_generating = True
        self.current_output = self.capacity * 0.8
        return f"Quyosh paneli #{self.panel_id} ishga tushdi"
    
    def get_output(self):
        return self.current_output if self.is_generating else 0
    
    def get_status(self):
        status = "ishlamoqda" if self.is_generating else "to'xtagan"
        return f"Quyosh paneli #{self.panel_id}: {status}, quvvat: {self.get_output()}kW"
    
    def stop(self):
        self.is_generating = False
        self.current_output = 0


class WindTurbine(PowerSource):
    def __init__(self, turbine_id, capacity):
        self.turbine_id = turbine_id
        self.capacity = capacity
        self.is_generating = False
        self.current_output = 0
    
    def generate(self):
        self.is_generating = True
        self.current_output = self.capacity * 0.6
        return f"Shamol turbinasi #{self.turbine_id} ishga tushdi"
    
    def get_output(self):
        return self.current_output if self.is_generating else 0
    
    def get_status(self):
        status = "ishlamoqda" if self.is_generating else "to'xtagan"
        return f"Shamol turbinasi #{self.turbine_id}: {status}, quvvat: {self.get_output()}kW"
    
    def stop(self):
        self.is_generating = False
        self.current_output = 0


class PowerGrid(PowerSource):
    def __init__(self, grid_name):
        self.grid_name = grid_name
        self.is_generating = False
        self.capacity = 10000
        self.load = 0
    
    def generate(self):
        self.is_generating = True
        return f"Elektr tarmog'i ({self.grid_name}) faol"
    
    def get_output(self):
        return self.capacity - self.load if self.is_generating else 0
    
    def get_status(self):
        status = "faol" if self.is_generating else "o'chiq"
        return f"Elektr tarmog'i ({self.grid_name}): {status}, yuklanish: {self.load}/{self.capacity}kW"
    
    def add_load(self, amount):
        self.load = min(self.capacity, self.load + amount)
    
    def remove_load(self, amount):
        self.load = max(0, self.load - amount)
