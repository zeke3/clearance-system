from django.apps import AppConfig


class AccountsConfig(AppConfig):
    name = 'accounts'

    def ready(self):
    	import accounts.signals


###### d3v3l0p3d by z3k3_03 ##############