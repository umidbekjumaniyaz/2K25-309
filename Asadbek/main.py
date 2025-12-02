import sys
sys.path.insert(0, '.')

from core.controller import SmartCityController


def print_menu():
    print("\n" + "="*50)
    print("       SMARTCITY BOSHQARUV TIZIMI")
    print("="*50)
    print("1. Tizim holati")
    print("2. Zonalar ro'yxati")
    print("3. Zona ma'lumotlari")
    print("4. Ob-havo ma'lumoti")
    print("5. Chiroqlarni yoqish")
    print("6. Chiroqlarni o'chirish")
    print("7. Xavfsizlik tizimi")
    print("8. Energiya tizimini ishga tushirish")
    print("9. Transport holati")
    print("0. Chiqish")
    print("="*50)


def show_security_menu(security):
    while True:
        print("\n--- Xavfsizlik tizimi ---")
        status = security.get_system_status()
        print(f"Joriy daraja: {status['access_level']}")
        print(f"Tizim: {'faol' if status['armed'] else 'nofaol'}")
        print()
        print("1. Daraja o'zgartirish (guest/user/admin)")
        print("2. Tizimni faollashtirish")
        print("3. Tizimni o'chirish")
        print("4. Kameralarni ko'rish")
        print("5. Signal berish")
        print("6. Kirish jurnali")
        print("0. Orqaga")
        
        choice = input("\nTanlang: ").strip()
        
        if choice == "1":
            level = input("Daraja (guest/user/admin): ").strip().lower()
            security.set_access_level(level)
            print(f"Daraja o'zgartirildi: {level}")
        elif choice == "2":
            print(security.arm_system())
        elif choice == "3":
            print(security.disarm_system())
        elif choice == "4":
            print(security.view_cameras())
        elif choice == "5":
            print(security.trigger_alarm())
        elif choice == "6":
            log = security.get_access_log()
            if log:
                print("\nKirish jurnali:")
                for entry in log:
                    print(f"  - {entry}")
            else:
                print("Jurnal bo'sh")
        elif choice == "0":
            break


def main():
    controller = SmartCityController()
    
    print("\nSmartCity tizimiga xush kelibsiz!")
    
    while True:
        print_menu()
        choice = input("\nTanlang: ").strip()
        
        if choice == "1":
            status = controller.get_system_status()
            print(f"\n{status['city_name']} holati:")
            print(f"  Zonalar soni: {status['zones']}")
            print(f"  Jami transport: {status['total_vehicles']}")
            print(f"  Jami chiroqlar: {status['total_lights']}")
            print(f"  Jami sensorlar: {status['total_sensors']}")
            print(f"  Energiya manbalari: {status['total_power_sources']}")
        
        elif choice == "2":
            zones = controller.get_all_zones()
            print("\nMavjud zonalar:")
            for zone in zones:
                print(f"  - {zone}")
        
        elif choice == "3":
            zones = controller.get_all_zones()
            print("Mavjud zonalar:", ", ".join(zones))
            zone_name = input("Zona nomini kiriting: ").strip()
            zone = controller.get_zone(zone_name)
            if zone:
                print(zone.get_info())
                print("\nChiroqlar:")
                for light in zone.lights:
                    print(f"  {light.get_status()}")
                print("\nSensorlar:")
                for sensor in zone.sensors:
                    print(f"  {sensor.check()}")
                print("\nEnergia manbalari:")
                for source in zone.power_sources:
                    print(f"  {source.get_status()}")
            else:
                print("Zona topilmadi!")
        
        elif choice == "4":
            weather = controller.get_weather()
            print(f"\n{weather.get_full_report()}")
        
        elif choice == "5":
            zones = controller.get_all_zones()
            print("Mavjud zonalar:", ", ".join(zones))
            zone_name = input("Zona nomini kiriting: ").strip()
            results = controller.activate_zone_lights(zone_name)
            if isinstance(results, list):
                for r in results:
                    print(f"  {r}")
            else:
                print(results)
        
        elif choice == "6":
            zones = controller.get_all_zones()
            print("Mavjud zonalar:", ", ".join(zones))
            zone_name = input("Zona nomini kiriting: ").strip()
            results = controller.deactivate_zone_lights(zone_name)
            if isinstance(results, list):
                for r in results:
                    print(f"  {r}")
            else:
                print(results)
        
        elif choice == "7":
            security = controller.get_security()
            show_security_menu(security)
        
        elif choice == "8":
            zones = controller.get_all_zones()
            print("Mavjud zonalar:", ", ".join(zones))
            zone_name = input("Zona nomini kiriting: ").strip()
            results = controller.start_zone_power(zone_name)
            if isinstance(results, list):
                for r in results:
                    print(f"  {r}")
            else:
                print(results)
        
        elif choice == "9":
            zones = controller.get_all_zones()
            print("Mavjud zonalar:", ", ".join(zones))
            zone_name = input("Zona nomini kiriting: ").strip()
            results = controller.get_zone_transport_status(zone_name)
            if isinstance(results, list):
                print(f"\n{zone_name} zonasidagi transportlar:")
                for r in results:
                    print(f"  {r}")
            else:
                print(results)
        
        elif choice == "0":
            print("\nXayr! SmartCity tizimidan chiqildi.")
            break
        
        else:
            print("Noto'g'ri tanlov!")


if __name__ == "__main__":
    main()
