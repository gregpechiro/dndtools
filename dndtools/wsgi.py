import os
import sys

#sys.path.append('/opt/dndtools')
#os.environ["DJANGO_SETTINGS_MODULE"] = "dndtools.settings"
#activate_this = '/opt/dndtools/env/bin/acivatate_this.py'
#execfile(activate_this, dict(__file__=activate_this))

sys.path = ['/opt/dndtools/' , '/opt/dndtools/dndtools/'] + sys.path
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dndtools.settings")
activate_this = '/opt/dndtools/env/bin/activate_this.py'
application = django.core.handlers.wsgi.WSGIHandler()
