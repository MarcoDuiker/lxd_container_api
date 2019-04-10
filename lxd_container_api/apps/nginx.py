from ._app import _app

class nginx(_app):
    '''
    This is really just an alias for the app postgresql.
    '''

    def __init__(self):
        self.name = 'nginx'

