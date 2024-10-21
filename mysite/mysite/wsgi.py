"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
import sys
from django.core.wsgi import get_wsgi_application

sys.path.append('/home/heichi/prj/django1/mysite')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

application = get_wsgi_application()



from os.path import join,dirname,abspath



# PROJECT_DIR = dirname(dirname(abspath(__file__)))
# sys.path.insert(0,PROJECT_DIR)

