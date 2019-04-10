import subprocess

class nginx(object):


    def __init__(self):
        self.name = 'apache2'

    def _execute(self, command):
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

    def start(self):
        '''Starts the service'''
 
        return self._execute(['service',self.name,'start'])

    def stop(self):
        '''Stops the service'''

        return self._execute(['service',self.name,'stop'])
        

    def exec(self, command, *args, **kwargs):
        pass

    @property
    def status(self):
        '''Returns status'''

        return self._execute(['service',self.name,'status']).stdout.decode("utf-8") 

    @property
    def is_running(self):
        '''Returns `True` if the service is running'''
        
        if 'Active: active' in self.status:
            return True

    @property
    def is_stopped(self):
        '''Returns `True` if the service is stopped'''

        if 'Active: inactive' in self.status:
            return True
