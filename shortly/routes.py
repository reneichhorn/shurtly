def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('createShortURL', '/') 
    config.add_route('redirectToShortURL', '/{shorturl}') 
    config.add_route('b', '/b')
