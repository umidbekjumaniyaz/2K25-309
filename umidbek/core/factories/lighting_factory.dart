// LightingFactory: Factory Method orqali LightingSystem yaratadi.
import '../../modules/lighting/lighting.dart';
import 'factory.dart';

class LightingFactory implements SubsystemFactory<LightingSystem> {
  @override
  LightingSystem create() => LightingSystem();
}
