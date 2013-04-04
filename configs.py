import os

TEMPLATE_PATH = os.path.join(os.path.dirname(__file__), "templates")
STATIC_PATH = os.path.join(os.path.dirname(__file__), "statics")
PORT = 8881


DATABASE = {
    'database': 'task',
    'host':     'localhost',
    'user':     'root',
    'password': '901014',
}
