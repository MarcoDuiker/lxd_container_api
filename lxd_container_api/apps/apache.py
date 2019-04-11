from ._app import _app

class apache(_app):

    def __init__(self):
        self.name = 'apache2'

        # we'll only use the sites-enabled folder 
        self.config_folder = '/etc/apache2/sites-enabled'
