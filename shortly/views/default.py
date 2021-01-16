from pyramid.view import view_config, view_defaults
import random, string
from shortly import shurtlydb
from pyramid.httpexceptions import HTTPFound

from pyramid.view import notfound_view_config


@notfound_view_config(renderer='../templates/404.jinja2')
def notfound_view(request):
    request.response.status = 404
    return {}

#@view_config(route_name='home', renderer='../templates/mytemplate.jinja2')
@view_config(route_name='b', renderer='../templates/mytemplateb.jinja2')
def my_view(request):
    return {'project': 'shortly'}

@view_defaults(route_name='createShortURL')
class ShortlyViews(object):
    def __init__(self, request):
        self.request = request
        self.view_name = 'ShortlyViews'

    @property
    def getLongUrl(self):
        url = self.request.matchdict['longurl']
        return url

    def createShort(self):
        return ''.join(random.choice(string.ascii_lowercase
         + string.ascii_uppercase + string.digits) for _ in range(11))

    @view_config(request_method= 'GET', renderer='../templates/shortly.jinja2')
    def shorten(self):
        return {'page_title': 'Shorten it'}

    @view_config(request_method='POST', renderer='../templates/shortened.jinja2')
    def create(self):
        shurtly = shurtlydb.Datab()
        shurtly.createConnect()
        longURL = self.request.params['longURL']
        rows = ['1', '2']
        while len(rows)>0:
            shortURL = self.createShort()
            rows = shurtly.selectWHERE(shortURL)
        shurtly.insert(longURL, shortURL)
        shurtly.closeConnection()
        return {'shortURL': shortURL, 'longURL': longURL}

@view_defaults(route_name='redirectToShortURL')

class RedirctShortViews(object):
    def __init__(self, request):
        self.request = request
        self.view_name = 'RedirctShortViews'

    @property
    def getShortURL(self):
        url = self.request.matchdict['shorturl']
        return url

    @view_config(request_method='GET', renderer='../templates/404.jinja2')
    def redirectToURL(self):
        shurtly = shurtlydb.Datab()
        shurtly.createConnect()
        shortURL =  self.request.matchdict['shorturl']
        rows = shurtly.selectWHERE(shortURL)
        try:
            url = rows[0][0]
        except:
            return notfound_view(self.request)
        else:
            return HTTPFound(location=url)



