"""
WSGI config for newsproject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os
from dotenv import load_dotenv
project_folder = os.path.expanduser('~/Desktop/code-platoon/week-14/personal_project/newsproject') 
load_dotenv(os.path.join(project_folder, '.env'))
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
