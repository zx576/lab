import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lab.server_settings")
django.setup()

from myproxy.utils.fetch import crwal


if __name__ == '__main__':
    crwal()
