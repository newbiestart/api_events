from django.apps import AppConfig

class ConfigConfig(AppConfig):
    name = "config"

    def ready(self):
        try:
            from django.contrib.sites.models import Site
            Site.objects.get(domain="127.0.0.1:8000")
        except:
            Site.objects.all().delete()
            Site.objects.create(
                id=1,
                domain="127.0.0.1:8000",
                name="Localhost"
            )
