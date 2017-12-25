#!/usr/bin/python3

from wsgiref.simple_server import make_server
from pyramid.config import Configurator

import radioclash


if __name__ == '__main__':
    with Configurator() as config:
        config.add_route('hello', '/')
        config.add_route('alive', '/alive')
        config.add_route('dir', '/dir')
        #config.add_route('item', '/item')
        config.add_route('get_config', '/get_config')
        config.add_route('write_config', '/write_config')
        config.scan('views')
        app = config.make_wsgi_app()
        server = make_server('0.0.0.0', 6543, app)
        server.serve_forever()