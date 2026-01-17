// EnergySystem: energiya sarfini kuzatish.
import '../../core/builders/energy_report_builder.dart';

class EnergySystem {
  double readConsumption() {
    // Demo uchun doimiy qiymat (kWh).
    return 1250.4;
  }

  void displayReport(EnergyReport report) {
    print('Energiya hisoboti: ${report.pretty()}');
  }
}
