import subprocess
from ._app import _app

class tomcat(_app):

    def __init__(self):
        self.name = 'tomcat'

    @property
    def status(self):
        '''Returns a status string.'''

        return self._execute(['systemctl', 'status', self.name]).stdout.decode("utf-8") 

    def start(self, *args, **kwargs):
        '''Starts the program or service with the optionally given arguments.'''

        return self._execute(['systemctl', 'start', self.name]).stdout.decode("utf-8")

    def stop(self):
        '''Stops the program or service.'''

        return self._execute(['systemctl', 'stop', self.name]).stdout.decode("utf-8")
