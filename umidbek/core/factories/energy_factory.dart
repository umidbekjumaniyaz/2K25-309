// EnergyFactory: Factory Method orqali EnergySystem yaratadi.
import '../../modules/energy/energy.dart';
import 'factory.dart';

class EnergyFactory implements SubsystemFactory<EnergySystem> {
  @override
  EnergySystem create() => EnergySystem();
}
