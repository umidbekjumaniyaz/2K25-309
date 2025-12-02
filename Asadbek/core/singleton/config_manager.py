class ConfigManager:
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
        self._settings = {
            "city_name": "SmartCity",
            "lighting_mode": "auto",
            "security_level": "medium",
            "energy_saving": True,
            "transport_active": True
        }
    
    def get(self, key):
        return self._settings.get(key)
    
    def set(self, key, value):
        self._settings[key] = value
    
    def get_all(self):
        return self._settings.copy()
