// WeatherAdapter: Adapter pattern. Tashqi ob-havo servisi javobini soddalashtirib qaytaradi.
import 'adapter.dart';

class FakeWeatherService {
  // Tashqi servisga o'xshash minimal sinf.
  String getCurrentCondition() => 'Quyoshli, +22C';
}

class WeatherAdapter implements ExternalServiceAdapter {
  WeatherAdapter() : _service = FakeWeatherService();

  final FakeWeatherService _service;

  @override
  String fetch() => _service.getCurrentCondition();

  String fetchWeatherSummary() => fetch();
}
