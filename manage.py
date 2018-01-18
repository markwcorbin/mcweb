#!/usr/bin/env python
import os
import sys
from django.conf import settings
sys.path.insert(0, 'manage_IP')
from get_mcweb_IP import *

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mcweb.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    
    # Get public IP address and set in mcweb/settings.py file if not DEBUG
    if settings.DEBUG == False:
        get_mcweb_IP()
    
    execute_from_command_line(sys.argv)
