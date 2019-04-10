import subprocess

class _app(object):
    '''
    A base class to derive an app from.

    All services which work with the familiar

    `sudo service app_name_goes_here start`

    type of thing can easily be derived from this class 
    only by setting `self.name` to `app_name_goes_here`.

    Other apps should overide the properties and methods 
    from this base class.
    '''

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
