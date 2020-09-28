from django.apps import AppConfig


class usuariosConfig(AppConfig):
    name = 'usuarios'

    def ready(self):
        import usuarios.signals