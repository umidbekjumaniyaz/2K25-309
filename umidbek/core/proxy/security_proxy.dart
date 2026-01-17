// SecurityProxy: Proxy pattern. Kirish tokenini tekshirib, keyin real tizimni chaqiradi.
import '../../modules/security/security.dart';
import 'proxy.dart';

class SecurityProxy implements SubsystemProxy {
  SecurityProxy(this._realSystem, {required this.requiredToken});

  final SecuritySystem _realSystem;
  final String requiredToken;

  void check(String providedToken) {
    if (providedToken == requiredToken) {
      execute();
    } else {
      _realSystem.logDenied();
    }
  }

  @override
  void execute() {
    _realSystem.monitor();
  }
}
