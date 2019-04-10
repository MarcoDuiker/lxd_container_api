#import subprocess

#class tomcat(object):
from ._app import _app

class tomcat(_app):

    def __init__(self):
        self.name = 'tomcat'

    def _execute(self, command, **kwargs):
        '''
        Accepts command as a list, and executes using subproces.

        Returns a subprocess. CompletedProcess object.
        '''

        return   subprocess.run(command, 
                                stdin = subprocess.PIPE, 
                                stdout = subprocess.PIPE, 
                                stderr = subprocess.PIPE,
                                check = True,
                                **kwargs)

    @property
    def status(self):
        '''Returns a status string.'''

        return self._execute(['systemctl', 'status', self.name]).stdout.decode("utf-8") 

    @property
    def is_running(self):
        '''Returns `True` if the program or service is running.'''

        if 'Active: active' in self.status:
            return True


    @property
    def is_stopped(self):
        '''Returns `True` if the program or service is NOT running.'''

        if 'Active: inactive' in self.status:
            return True


    def start(self, *args, **kwargs):
        '''Starts the program or service with the optionally given arguments.'''

        return self._execute(['systemctl', 'start', self.name]).stdout.decode("utf-8")

    def stop(self):
        '''Stops the program or service.'''

        return self._execute(['systemctl', 'stop', self.name]).stdout.decode("utf-8")

    def exec(self, command, *args, **kwargs):
        '''Executes an arbitrary command with the given name and arguments.'''

        pass

