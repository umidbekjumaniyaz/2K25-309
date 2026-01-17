// SmartCity System konsol ilovasi.
// Bu faylda foydalanuvchi bilan muloqot va markaziy controller chaqiriladi.

import 'dart:io';

import 'core/controller.dart';

void main(List<String> args) {
  final controller = CentralController();
  _showWelcome();

  bool running = true;
  while (running) {
    _showMenu();
    stdout.write('> Tanlov: ');
    final input = stdin.readLineSync()?.trim() ?? '';

    switch (input) {
      case '1':
        controller.toggleLighting();
        break;
      case '2':
        controller.monitorTransport();
        break;
      case '3':
        stdout.write('> Xavfsizlik uchun ruxsat kodi kiriting: ');
        final token = stdin.readLineSync()?.trim() ?? '';
        controller.checkSecurity(token);
        break;
      case '4':
        controller.generateEnergyReport();
        break;
      case '0':
        running = false;
        stdout.writeln('Dastur yakunlandi.');
        break;
      default:
        stdout.writeln('Nomaqbul tanlov, qayta urinib ko\'ring.');
    }
  }
}

void _showWelcome() {
  stdout.writeln('== SmartCity System ==');
  stdout.writeln('Shahar infratuzilmasini boshqarish simulyatori.');
}

void _showMenu() {
  stdout.writeln('\n1) Yoritishni boshqarish');
  stdout.writeln('2) Transport monitoring');
  stdout.writeln('3) Xavfsizlikni tekshirish');
  stdout.writeln('4) Energiya hisobotini yaratish');
  stdout.writeln('0) Chiqish');
}
