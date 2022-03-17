import json
import os.path
import random
import sqlite3
import time
import uuid

from jinja2 import Environment
from jinja2 import FileSystemLoader

from routes.session import session

path = '{}/templates/'.format(os.path.dirname(__file__))

loader = FileSystemLoader(path)
env = Environment(loader=loader)


def log(*args, **kwargs):
    format = '%H:%M:%S'
    value = time.localtime(int(time.time()))
    dt = time.strftime(format, value)
    with open('log.txt', 'a', encoding='utf-8') as f:
        print(dt, *args, file=f, **kwargs)


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


def random_key():
    return uuid.uuid4().hex


"""
def template(name):
    path = 'templates/' + name
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()
"""

def template(path, **kwargs):
    """load tpl with jinja
    """
    t = env.get_template(path)
    return t.render(**kwargs)


def current_user(request):
    session_id = request.cookies.get('user', '')
    uid = session.get(session_id, '')
    return uid


def response_with_headers(headers, status_code=200):
    header = 'HTTP/1.1 {} OK\r\n'.format(status_code)
    header += ''.join(['{}: {}\r\n'.format(k, v) for k, v in headers.items()])
    return header


def redirect(url):
    headers = {
        'Content-Type': 'text/html',
    }
    headers['Location'] = url
    header = response_with_headers(headers, 302)
    r = header + '\r\n' + ''
    return r.encode(encoding='utf-8')


"""
def error(request, code=404):
    e = {
        404: b'HTTP/1.1 404 NOT FOUND\r\n\r\n<h1>404 Not Found</h1>',
    }
    return e.get(code, b'')
"""

def error(request, code=404):
    header = 'HTTP/1.1 404 NOT FOUND\r\n\r\n'
    e = {
        404: http_response(template('404.html')),
    }
    return e.get(code, b'')


def http_response(body, headers=None):
    """send response
    """
    header = 'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n'
    if headers is not None:
        header += ''.join(['{}: {}\r\n'.format(k, v) for k, v in headers.items()])
    r = header + '\r\n' + body
    return r.encode(encoding='utf-8')


def json_response(data):
    """this function is used for ajax

    def route(request):
        return json_response(t.json())
    """
    header = 'HTTP/1.1 200 OK\r\nContent-Type: application/json\r\n'
    body = json.dumps(data, ensure_ascii=False, indent=8)
    r = header + '\r\n' + body
    return r.encode(encoding='utf-8')
