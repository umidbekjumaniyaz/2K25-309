# SmartCity System (Dart)

Konsol ilova: shahar infratuzilmasini (yoritish, transport, xavfsizlik, energiya) boshqarishni soddalashtirilgan tarzda simulyatsiya qiladi. Kod va kommentlar uzbek tilida.

## Arxitektura va patternlar
- Singleton + Facade: `CentralController` (barcha subsystemlarga yagona kirish).
- Factory Method: har bir modul uchun alohida factory (`LightingFactory`, `TransportFactory`, `SecurityFactory`, `EnergyFactory`).
- Adapter: `WeatherAdapter` tashqi ob-havo xizmatini soddalashtiradi.
- Proxy: `SecurityProxy` token bilan kirishni filtrlash.
- Builder: `EnergyReportBuilder` energiya hisobotini bosqichma-bosqich yaratadi.

## Loyihaning tuzilishi
- `main.dart` — konsol menyu va foydalanuvchi interaktsiyasi.
- `core/` — controller, factory, builder, adapter, proxy, singleton.
- `modules/` — yoritish, transport, xavfsizlik, energiya subsystemlari.
- `test/` — birlik testlar (`controller_test.dart`).

## Ishga tushirish
1) Ilovani ishga tushirish:
	```bash
	dart run umidbek/main.dart
	```
2) Menyu orqali variantlarni tanlang (1–4), xavfsizlik uchun demo token: `1234`.

## Testlar
1) Testlarni ishga tushirish:
	```bash
	dart test
	```
2) Asosiy qamrov: yoritish toggle, transport monitoring, xavfsizlik (to'g'ri/noto'g'ri token), energiya hisobot va ob-havo adaptori, singleton tekshiruvi.

## Minimal talablar bajarilgan
- Kamida 5 pattern ishlatilgan (Singleton, Facade, Factory Method, Adapter, Proxy, Builder).
- Konsol interfeys mavjud.
- Har pattern maqsadi va kodi izohlangan.
