def on_starting(server):
    from django.core.management import call_command
    call_command('syncmedia')

import os
pythonpath = os.path.abspath("..")
bind = "0.0.0.0:8000"
workers = 3
daemon = False
loglevel = "debug"
proc_name = "{{ project_name }}"
worker_class = "gevent"
debug = True
django_settings = "{{ project_name }}.settings"
