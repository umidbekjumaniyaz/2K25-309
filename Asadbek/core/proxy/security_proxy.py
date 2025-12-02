from abc import ABC, abstractmethod


class SecuritySystemInterface(ABC):
    @abstractmethod
    def arm_system(self):
        pass
    
    @abstractmethod
    def disarm_system(self):
        pass
    
    @abstractmethod
    def view_cameras(self):
        pass
    
    @abstractmethod
    def trigger_alarm(self):
        pass


class RealSecuritySystem(SecuritySystemInterface):
    def __init__(self):
        self.is_armed = False
        self.cameras_active = False
    
    def arm_system(self):
        self.is_armed = True
        self.cameras_active = True
        return "Xavfsizlik tizimi faollashtirildi"
    
    def disarm_system(self):
        self.is_armed = False
        return "Xavfsizlik tizimi o'chirildi"
    
    def view_cameras(self):
        if self.cameras_active:
            return "Kameralar ko'rsatilmoqda..."
        return "Kameralar o'chiq"
    
    def trigger_alarm(self):
        return "OGOHLANTIRISH! Signal berildi!"


class SecurityProxy(SecuritySystemInterface):
    def __init__(self):
        self._real_system = RealSecuritySystem()
        self._access_level = "guest"
        self._access_log = []
    
    def set_access_level(self, level):
        if level in ["guest", "user", "admin"]:
            self._access_level = level
    
    def _log_access(self, action, allowed):
        status = "ruxsat berildi" if allowed else "rad etildi"
        self._access_log.append(f"{action}: {status} ({self._access_level})")
    
    def arm_system(self):
        if self._access_level in ["user", "admin"]:
            self._log_access("arm_system", True)
            return self._real_system.arm_system()
        self._log_access("arm_system", False)
        return "Ruxsat yo'q! Faqat user yoki admin faollashtira oladi"
    
    def disarm_system(self):
        if self._access_level == "admin":
            self._log_access("disarm_system", True)
            return self._real_system.disarm_system()
        self._log_access("disarm_system", False)
        return "Ruxsat yo'q! Faqat admin o'chira oladi"
    
    def view_cameras(self):
        if self._access_level in ["user", "admin"]:
            self._log_access("view_cameras", True)
            return self._real_system.view_cameras()
        self._log_access("view_cameras", False)
        return "Ruxsat yo'q! Kameralarni ko'rish uchun user yoki admin bo'lish kerak"
    
    def trigger_alarm(self):
        self._log_access("trigger_alarm", True)
        return self._real_system.trigger_alarm()
    
    def get_access_log(self):
        return self._access_log.copy()
    
    def get_system_status(self):
        return {
            "armed": self._real_system.is_armed,
            "cameras": self._real_system.cameras_active,
            "access_level": self._access_level
        }
