// Unit testlar: asosiy funksiyalar va patternlar tekshiruvi.

import 'dart:async';

import 'package:test/test.dart';

import '../core/controller.dart';
import '../core/builders/energy_report_builder.dart';
import '../core/adapters/weather_adapter.dart';

Future<String> capturePrint(Future<void> Function() body) async {
  final buffer = StringBuffer();
  await runZoned(
    body,
    zoneSpecification: ZoneSpecification(
      print: (self, parent, zone, line) {
        buffer.writeln(line);
      },
    ),
  );
  return buffer.toString();
}

void main() {
  final controller = CentralController();

  setUp(() {
    controller.resetStateForTest();
  });

  test('Controller Singleton qaytaradi', () {
    final a = CentralController();
    final b = CentralController();
    expect(identical(a, b), isTrue);
  });

  test('Yoritish yoqilib-o\'chirildi', () async {
    final out = await capturePrint(() async {
      controller.toggleLighting();
      controller.toggleLighting();
    });

    expect(out, contains('Yoritish tizimi yoqildi'));
    expect(out, contains('Yoritish tizimi o\'chirildi'));
  });

  test('Reset holat yoritishni boshidan yoqadi', () async {
    await capturePrint(() async {
      controller.toggleLighting(); // yoqildi
    });
    controller.resetStateForTest();

    final out = await capturePrint(() async {
      controller.toggleLighting(); // yana yoqilishi kerak
    });

    expect(out, contains('Yoritish tizimi yoqildi'));
  });

  test('Transport monitoring ishlaydi', () async {
    final out = await capturePrint(() async {
      controller.monitorTransport();
    });

    expect(out, contains('Transport monitoring'));
  });

  test('Xavfsizlik noto\'g\'ri tokenni rad etadi', () async {
    final out = await capturePrint(() async {
      controller.checkSecurity('wrong');
    });

    expect(out, contains('ruxsat kod noto\'g\'ri'));
  });

  test('Xavfsizlik to\'g\'ri token bilan o\'tadi', () async {
    final out = await capturePrint(() async {
      controller.checkSecurity('1234');
    });

    expect(out, contains('kameralar onlayn'));
  });

  test('Energiya hisobotida ob-havo va sarf chiqadi', () async {
    final out = await capturePrint(() async {
      controller.generateEnergyReport();
    });

    expect(out, contains('Energiya hisoboti'));
    expect(out, contains('1250.4 kWh'));
    expect(out, contains('Quyoshli, +22C'));
  });

  test('EnergyReport pretty format to\'g\'ri', () {
    final report = EnergyReport(consumptionKwh: 10.5, weatherSummary: 'Bulutli');
    expect(report.pretty(), 'Energiya sarfi: 10.5 kWh | Ob-havo: Bulutli');
  });

  test('WeatherAdapter ASCII format beradi', () {
    final adapter = WeatherAdapter();
    final weather = adapter.fetchWeatherSummary();
    expect(weather, 'Quyoshli, +22C');
  });
}
