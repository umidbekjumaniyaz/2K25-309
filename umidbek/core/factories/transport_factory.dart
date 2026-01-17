// TransportFactory: Factory Method orqali TransportSystem yaratadi.
import '../../modules/transport/transport.dart';
import 'factory.dart';

class TransportFactory implements SubsystemFactory<TransportSystem> {
  @override
  TransportSystem create() => TransportSystem();
}
