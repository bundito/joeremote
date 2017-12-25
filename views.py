from pyramid.response import Response
from pyramid.view import view_config
from pyramid.wsgi import wsgiapp
import json

import my_app as my_app


@wsgiapp
@view_config(route_name='hello')
def hello_view(request):
    return Response("Hello.")

@view_config(route_name='alive')
def alive_view(request):
    return Response("True")

@view_config(route_name='dir')
def dir_view(request):
    from rsc.DownloadListing import list
    return Response(json.dumps(list))
    #return Response("Yes?")


@view_config(route_name='get_config')
def get_config_view(request):
    with open("application.conf", "r") as f:
        cfg = f.read()
    return Response(cfg)


@view_config(route_name='write_config', renderer='string')
def post_write_config(request):
    #jayson = {"content": Response.}
    j2 = ""
    jayson = request.json_body

    with open("application.conf", "w") as f:
        f.write(json.dumps(jayson))
    print(jayson)
    print(j2)


"""
@view_config(route_name='exception')
def exception_view(request):
    raise Exception()
"""