// Markaziy controller: Facade + Singleton.
// Vazifasi: barcha subsystemlarni bir joydan boshqarish va sodda API berish.

import '../modules/lighting/lighting.dart';
import '../modules/transport/transport.dart';
import '../modules/security/security.dart';
import '../modules/energy/energy.dart';
import 'factories/factory.dart';
import 'factories/lighting_factory.dart';
import 'factories/transport_factory.dart';
import 'factories/security_factory.dart';
import 'factories/energy_factory.dart';
import 'proxy/security_proxy.dart';
import 'adapters/weather_adapter.dart';
import 'builders/energy_report_builder.dart';

class CentralController {
  // Singleton instance.
  static final CentralController _instance = CentralController._internal();
  factory CentralController() => _instance;

  CentralController._internal()
      : _lightingFactory = LightingFactory(),
        _transportFactory = TransportFactory(),
        _securityFactory = SecurityFactory(),
        _energyFactory = EnergyFactory(),
        _weatherAdapter = WeatherAdapter();

  final SubsystemFactory<LightingSystem> _lightingFactory;
  final SubsystemFactory<TransportSystem> _transportFactory;
  final SubsystemFactory<SecuritySystem> _securityFactory;
  final SubsystemFactory<EnergySystem> _energyFactory;
  final WeatherAdapter _weatherAdapter;

  LightingSystem? _lighting;
  TransportSystem? _transport;
  SecuritySystem? _security;
  EnergySystem? _energy;

  // Facade metodlari: konsol menudan chaqiriladi.
  void toggleLighting() {
    final lighting = _lighting ??= _lightingFactory.create();
    lighting.toggle();
  }

  void monitorTransport() {
    final transport = _transport ??= _transportFactory.create();
    transport.monitor();
  }

  void checkSecurity(String token) {
    final security = _security ??= _securityFactory.create();
    final proxy = SecurityProxy(security, requiredToken: '1234');
    proxy.check(token);
  }

  void generateEnergyReport() {
    final energy = _energy ??= _energyFactory.create();
    final builder = EnergyReportBuilder()
      ..withConsumption(energy.readConsumption())
      ..withWeather(_weatherAdapter.fetchWeatherSummary());
    final report = builder.build();
    energy.displayReport(report);
  }

  // Testlarga qulaylik uchun holatni tiklash.
  void resetStateForTest() {
    _lighting = null;
    _transport = null;
    _security = null;
    _energy = null;
  }
}
