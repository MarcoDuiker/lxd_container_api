from ._app import _app

class nginx(_app):
    
    def __init__(self):
        self.name = 'nginx'

        # we'll only use the sites-enabled folder        
        self.config_folder = '/etc/nginx/sites-enabled'
