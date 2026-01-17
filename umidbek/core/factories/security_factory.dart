// SecurityFactory: Factory Method orqali SecuritySystem yaratadi.
import '../../modules/security/security.dart';
import 'factory.dart';

class SecurityFactory implements SubsystemFactory<SecuritySystem> {
  @override
  SecuritySystem create() => SecuritySystem();
}
