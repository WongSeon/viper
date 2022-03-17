import socket
import _thread

from utils import log
from utils import error
from routes.routes_static import route_static
from routes.routes_index import route_dict
from request import Request


def parsed_path(path):
    index = path.find('?')
    if index == -1:
        return path, {}
    else:
        path, query_string = path.split('?', 1)
        args = query_string.split('&')
        query = {}
        for arg in args:
            k, v = arg.split('=')
            query[k] = v
        return path, query


def response_for_path(path, request):
    path, query = parsed_path(path)
    request.path = path
    request.query = query
    route = {
        '/static': route_static,
    }
    route.update(route_dict)
    response = route.get(path, error)
    return response(request)


def process_request(connection):
    receives = b''
    buffer_size = 1024
    while True:
        ret = connection.recv(buffer_size)
        receives += ret
        if len(ret) < buffer_size:
            break
    receives = receives.decode('utf-8')
    log('receives\r\n{}'.format(receives))
    if len(receives.split()) < 2:
        connection.close()
    else:
        path = receives.split()[1]
        request = Request()
        request.method = receives.split()[0]
        request.body = receives.split('\r\n\r\n', 1)[1]
        response = response_for_path(path, request)
        connection.sendall(response)
        connection.close()


def run(host='', port=12345):
    log('start at', '{}:{}'.format(host, port))
    with socket.socket() as s:
        s.bind((host, port))
        s.listen(5)
        while True:
            connection, address = s.accept()
            _thread.start_new_thread(process_request, (connection,))


def main():
    config = dict(
        host='',
        port=12345,
    )
    run(**config)
