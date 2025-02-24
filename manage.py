#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import subprocess


def start_background_services():
    """ Start Redis, Celery worker, and Celery Flower when running the Django server """
    subprocess.Popen(["redis-server"])
    subprocess.Popen(["celery", "-A", "blog_application", "worker", "--loglevel=info"])
    subprocess.Popen(["celery", "-A", "blog_application", "beat", "--loglevel=info"])
    subprocess.Popen(["celery", "-A", "blog_application", "flower"])


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog_application.settings')
    try:
        if "runserver" in sys.argv:
            start_background_services()
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
