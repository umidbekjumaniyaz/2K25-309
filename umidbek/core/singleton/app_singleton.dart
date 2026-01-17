// Singleton placeholder to ensure unique shared resources.
class AppSingleton {
  AppSingleton._internal();
  static final AppSingleton _instance = AppSingleton._internal();
  factory AppSingleton() => _instance;
}
