import sys
sys.path.insert(0, '.')

import unittest
from core.singleton.config_manager import ConfigManager
from core.factories.transport_factory import TransportCreator
from core.factories.lighting_factory import LightingCreator
from core.builders.zone_builder import ZoneBuilder, CityZone
from core.adapters.weather_adapter import WeatherAdapter
from core.proxy.security_proxy import SecurityProxy
from core.controller import SmartCityController
from modules.transport.vehicles import Bus, Taxi, Metro
from modules.lighting.lights import StreetLight, TrafficLight, ParkLight
from modules.security.sensors import MotionSensor, Camera, AlarmSystem
from modules.energy.power_systems import SolarPanel, WindTurbine, PowerGrid


class TestSingleton(unittest.TestCase):
    def test_config_manager_singleton(self):
        config1 = ConfigManager()
        config2 = ConfigManager()
        self.assertIs(config1, config2)
    
    def test_config_manager_settings(self):
        config = ConfigManager()
        config.set("test_key", "test_value")
        self.assertEqual(config.get("test_key"), "test_value")
    
    def test_controller_singleton(self):
        controller1 = SmartCityController()
        controller2 = SmartCityController()
        self.assertIs(controller1, controller2)


class TestFactoryMethod(unittest.TestCase):
    def test_create_bus(self):
        bus = TransportCreator.create("bus", 15)
        self.assertIsInstance(bus, Bus)
        self.assertEqual(bus.route_number, 15)
    
    def test_create_taxi(self):
        taxi = TransportCreator.create("taxi", "ABC123")
        self.assertIsInstance(taxi, Taxi)
        self.assertEqual(taxi.car_id, "ABC123")
    
    def test_create_metro(self):
        metro = TransportCreator.create("metro", "Ko'k")
        self.assertIsInstance(metro, Metro)
        self.assertEqual(metro.line_name, "Ko'k")
    
    def test_invalid_vehicle_type(self):
        with self.assertRaises(ValueError):
            TransportCreator.create("helicopter", "H001")
    
    def test_create_street_light(self):
        light = LightingCreator.create("street", "Test ko'cha")
        self.assertIsInstance(light, StreetLight)
    
    def test_create_traffic_light(self):
        light = LightingCreator.create("traffic", "Test choraha")
        self.assertIsInstance(light, TrafficLight)
    
    def test_create_park_light(self):
        light = LightingCreator.create("park", "Test park")
        self.assertIsInstance(light, ParkLight)


class TestBuilder(unittest.TestCase):
    def test_zone_builder_creates_zone(self):
        zone = ZoneBuilder("Test").build()
        self.assertIsInstance(zone, CityZone)
        self.assertEqual(zone.name, "Test")
    
    def test_zone_builder_chain(self):
        zone = (ZoneBuilder("Test")
            .add_bus(1)
            .add_taxi("T1")
            .add_street_light("Ko'cha")
            .add_camera("Bino")
            .add_solar_panel(1, 100)
            .build())
        
        self.assertEqual(len(zone.vehicles), 2)
        self.assertEqual(len(zone.lights), 1)
        self.assertEqual(len(zone.sensors), 1)
        self.assertEqual(len(zone.power_sources), 1)
    
    def test_zone_info(self):
        zone = ZoneBuilder("Test").add_bus(1).build()
        info = zone.get_info()
        self.assertIn("Test", info)


class TestAdapter(unittest.TestCase):
    def test_weather_adapter_temperature(self):
        adapter = WeatherAdapter()
        temp = adapter.get_temperature()
        self.assertIsInstance(temp, float)
    
    def test_weather_adapter_wind(self):
        adapter = WeatherAdapter()
        wind = adapter.get_wind_speed()
        self.assertIsInstance(wind, float)
    
    def test_weather_adapter_humidity(self):
        adapter = WeatherAdapter()
        humidity = adapter.get_humidity()
        self.assertIsInstance(humidity, int)
    
    def test_weather_full_report(self):
        adapter = WeatherAdapter()
        report = adapter.get_full_report()
        self.assertIn("Ob-havo", report)
        self.assertIn("Harorat", report)


class TestProxy(unittest.TestCase):
    def test_proxy_guest_cannot_arm(self):
        proxy = SecurityProxy()
        proxy.set_access_level("guest")
        result = proxy.arm_system()
        self.assertIn("Ruxsat yo'q", result)
    
    def test_proxy_user_can_arm(self):
        proxy = SecurityProxy()
        proxy.set_access_level("user")
        result = proxy.arm_system()
        self.assertIn("faollashtirildi", result)
    
    def test_proxy_user_cannot_disarm(self):
        proxy = SecurityProxy()
        proxy.set_access_level("user")
        result = proxy.disarm_system()
        self.assertIn("Ruxsat yo'q", result)
    
    def test_proxy_admin_can_disarm(self):
        proxy = SecurityProxy()
        proxy.set_access_level("admin")
        proxy.arm_system()
        result = proxy.disarm_system()
        self.assertIn("o'chirildi", result)
    
    def test_proxy_access_log(self):
        proxy = SecurityProxy()
        proxy.arm_system()
        log = proxy.get_access_log()
        self.assertEqual(len(log), 1)


class TestVehicles(unittest.TestCase):
    def test_bus_move_stop(self):
        bus = Bus(10)
        bus.move()
        self.assertTrue(bus.is_moving)
        bus.stop()
        self.assertFalse(bus.is_moving)
    
    def test_bus_passengers(self):
        bus = Bus(10)
        bus.board_passengers(5)
        self.assertEqual(bus.passengers, 5)
    
    def test_taxi_availability(self):
        taxi = Taxi("T001")
        self.assertTrue(taxi.is_available)
        taxi.move()
        self.assertFalse(taxi.is_available)
        taxi.complete_trip()
        self.assertTrue(taxi.is_available)
    
    def test_metro_station(self):
        metro = Metro("Qizil")
        metro.arrive_at_station("Buyuk Ipak Yo'li")
        self.assertEqual(metro.current_station, "Buyuk Ipak Yo'li")


class TestLights(unittest.TestCase):
    def test_street_light_on_off(self):
        light = StreetLight("Test")
        light.turn_on()
        self.assertTrue(light.is_on)
        light.turn_off()
        self.assertFalse(light.is_on)
    
    def test_street_light_brightness(self):
        light = StreetLight("Test")
        light.set_brightness(50)
        self.assertEqual(light.brightness, 50)
        light.set_brightness(150)
        self.assertEqual(light.brightness, 100)
    
    def test_traffic_light_colors(self):
        light = TrafficLight("Test")
        light.turn_on()
        light.change_color("green")
        self.assertEqual(light.current_color, "green")
    
    def test_park_light_mode(self):
        light = ParkLight("Test")
        light.set_mode("eco")
        self.assertEqual(light.mode, "eco")


class TestSensors(unittest.TestCase):
    def test_motion_sensor(self):
        sensor = MotionSensor("Test")
        sensor.activate()
        self.assertTrue(sensor.is_active)
        sensor.detect_motion()
        self.assertTrue(sensor.motion_detected)
        sensor.reset()
        self.assertFalse(sensor.motion_detected)
    
    def test_camera_recording(self):
        camera = Camera("Test")
        camera.activate()
        camera.start_recording()
        self.assertTrue(camera.is_recording)
        camera.stop_recording()
        self.assertFalse(camera.is_recording)
    
    def test_alarm_trigger(self):
        alarm = AlarmSystem("Test")
        alarm.activate()
        alarm.trigger()
        self.assertTrue(alarm.is_triggered)
        alarm.reset()
        self.assertFalse(alarm.is_triggered)


class TestPowerSystems(unittest.TestCase):
    def test_solar_panel(self):
        panel = SolarPanel(1, 100)
        panel.generate()
        self.assertEqual(panel.get_output(), 80)
        panel.stop()
        self.assertEqual(panel.get_output(), 0)
    
    def test_wind_turbine(self):
        turbine = WindTurbine(1, 100)
        turbine.generate()
        self.assertEqual(turbine.get_output(), 60)
    
    def test_power_grid_load(self):
        grid = PowerGrid("Test")
        grid.generate()
        grid.add_load(1000)
        self.assertEqual(grid.load, 1000)
        grid.remove_load(500)
        self.assertEqual(grid.load, 500)


class TestController(unittest.TestCase):
    def test_get_all_zones(self):
        controller = SmartCityController()
        zones = controller.get_all_zones()
        self.assertIn("markaz", zones)
        self.assertIn("turar-joy", zones)
        self.assertIn("sanoat", zones)
    
    def test_get_zone(self):
        controller = SmartCityController()
        zone = controller.get_zone("markaz")
        self.assertIsNotNone(zone)
        self.assertEqual(zone.name, "Markaz")
    
    def test_system_status(self):
        controller = SmartCityController()
        status = controller.get_system_status()
        self.assertIn("city_name", status)
        self.assertIn("zones", status)
        self.assertIn("total_vehicles", status)
    
    def test_activate_lights(self):
        controller = SmartCityController()
        results = controller.activate_zone_lights("markaz")
        self.assertIsInstance(results, list)
        self.assertTrue(len(results) > 0)
    
    def test_invalid_zone(self):
        controller = SmartCityController()
        result = controller.activate_zone_lights("noma'lum")
        self.assertIn("topilmadi", result)


if __name__ == "__main__":
    unittest.main(verbosity=2)
