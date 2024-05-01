#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from seed_api_app.mongo_migrations import initial_seed_collection,initial_user_collection

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'seed_api_project.settings')
    initial_seed_collection.initial_seed_collection()
    initial_user_collection.initial_user_collection() 
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
