"""Gunicorn config."""
import multiprocessing
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = "uvicorn.workers.UvicornWorker"
bind = "0.0.0.0:8080"
pidfile = "log/gunicorn.pid"
accesslog = "log/gunicorn.log"
errorlog = "log/gunicorn.log"
preload_app = True
reload = True
daemon = False
timeout = 200
