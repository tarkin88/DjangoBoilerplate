import os

try:
    _environment = os.getenv('ENVIRONMENT', None)
    if _environment == "docker":
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Project.settings.docker")
    elif _environment == "local":
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Project.settings.local_debug_docker")
except Exception as error:
    print(error)
