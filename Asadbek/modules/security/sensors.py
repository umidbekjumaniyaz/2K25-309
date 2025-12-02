from abc import ABC, abstractmethod


class Sensor(ABC):
    @abstractmethod
    def activate(self):
        pass
    
    @abstractmethod
    def deactivate(self):
        pass
    
    @abstractmethod
    def check(self):
        pass


class MotionSensor(Sensor):
    def __init__(self, zone):
        self.zone = zone
        self.is_active = False
        self.motion_detected = False
    
    def activate(self):
        self.is_active = True
        return f"Harakat sensori ({self.zone}) faollashtirildi"
    
    def deactivate(self):
        self.is_active = False
        return f"Harakat sensori ({self.zone}) o'chirildi"
    
    def check(self):
        if not self.is_active:
            return f"Harakat sensori ({self.zone}): nofaol"
        status = "harakat aniqlandi!" if self.motion_detected else "tinch"
        return f"Harakat sensori ({self.zone}): {status}"
    
    def detect_motion(self):
        self.motion_detected = True
    
    def reset(self):
        self.motion_detected = False


class Camera(Sensor):
    def __init__(self, location):
        self.location = location
        self.is_active = False
        self.is_recording = False
    
    def activate(self):
        self.is_active = True
        return f"Kamera ({self.location}) yoqildi"
    
    def deactivate(self):
        self.is_active = False
        self.is_recording = False
        return f"Kamera ({self.location}) o'chirildi"
    
    def check(self):
        if not self.is_active:
            return f"Kamera ({self.location}): o'chiq"
        status = "yozmoqda" if self.is_recording else "kuzatmoqda"
        return f"Kamera ({self.location}): {status}"
    
    def start_recording(self):
        if self.is_active:
            self.is_recording = True
    
    def stop_recording(self):
        self.is_recording = False


class AlarmSystem(Sensor):
    def __init__(self, building):
        self.building = building
        self.is_active = False
        self.is_triggered = False
    
    def activate(self):
        self.is_active = True
        return f"Signal tizimi ({self.building}) faollashtirildi"
    
    def deactivate(self):
        self.is_active = False
        self.is_triggered = False
        return f"Signal tizimi ({self.building}) o'chirildi"
    
    def check(self):
        if not self.is_active:
            return f"Signal tizimi ({self.building}): nofaol"
        status = "OGOHLANTIRISH!" if self.is_triggered else "normal"
        return f"Signal tizimi ({self.building}): {status}"
    
    def trigger(self):
        if self.is_active:
            self.is_triggered = True
    
    def reset(self):
        self.is_triggered = False
