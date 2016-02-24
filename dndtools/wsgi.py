import os
import sys

sys.path = ['/opt/dndtools/' , '/opt/dndtools/dndtools/'] + sys.path
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dndtools.settings")
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
