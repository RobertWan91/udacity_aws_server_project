import sys
import logging

logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/var/www/catalog')

from project import app as application
application.secret_key='super_secret_key'
