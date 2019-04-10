from ._app import _app

class ufw(_app):

    def __init__(self):
        self.name = 'ufw'

    @property
    def status(self):
        '''Returns a status string.'''

        return self._execute([self.name,'status']).stdout.decode("utf-8") 

    @property
    def is_running(self):
        '''Returns `True` if the program or service is running.'''

        if 'Status: active' in self.status:
            return True

    @property
    def is_stopped(self):
        '''Returns `True` if the program or service is NOT running.'''

        if 'Status: inactive' in self.status:
            return True


    def start(self, *args, **kwargs):
        '''Starts the program or service with the optionally given arguments.'''

        return self._execute([self.name,'enable']).stdout.decode("utf-8")

    def stop(self):
        '''Stops the program or service.'''

        return self._execute([self.name,'disable']).stdout.decode("utf-8")
