web: gunicorn dividends_backend.wsgi --log-file -
worker: celery -A dividends_backend beat -l info