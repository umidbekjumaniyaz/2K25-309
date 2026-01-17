// LightingSystem: yoritish tizimini boshqaradi.
class LightingSystem {
  bool _isOn = false;

  void toggle() {
    _isOn = !_isOn;
    final status = _isOn ? 'yoqildi' : 'o\'chirildi';
    print('Yoritish tizimi $status.');
  }
}
