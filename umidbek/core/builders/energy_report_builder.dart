// EnergyReportBuilder: Builder pattern. Ma'lumotlarni bosqichma-bosqich to'plab hisobot yaratadi.
import 'builder.dart';

class EnergyReport {
  EnergyReport({required this.consumptionKwh, required this.weatherSummary});

  final double consumptionKwh;
  final String weatherSummary;

  String pretty() =>
      'Energiya sarfi: ${consumptionKwh.toStringAsFixed(1)} kWh | Ob-havo: $weatherSummary';
}

class EnergyReportBuilder implements SubsystemBuilder<EnergyReport> {
  double _consumptionKwh = 0;
  String _weatherSummary = 'Noma`lum';

  EnergyReportBuilder withConsumption(double value) {
    _consumptionKwh = value;
    return this;
  }

  EnergyReportBuilder withWeather(String summary) {
    _weatherSummary = summary;
    return this;
  }

  @override
  EnergyReport build() {
    return EnergyReport(
      consumptionKwh: _consumptionKwh,
      weatherSummary: _weatherSummary,
    );
  }
}
