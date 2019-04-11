import os
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

    If an app supports adding config by writing a file to a folder
    the configuration methods only need proper setting of the folder via

    `self.config_folder` in the __init__ method.
    '''

    def __init__(self):
        '''
        These properties are here defined as placeholders.
        These are redefine as needed in the __init__ methods 
        in each app.
        '''

        self.name = None    
        self.config_folder = None
        

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

    # config methods
    def _config_file_name(self, name):
        '''
        Returns the config file name for a
        config file in the config folder.
        '''

        return os.path.join(self.config_folder, name)

    def add_config(self, name, config):
        '''
        Adds an item to the config.
        '''

        fn = self._config_file_name(name)
        if not os.path.exists(fn):
            with open(fn, 'wb') as f:
                f.write(config)

    def drop_config(self, name):
        '''
        Removes an item from the config.
        '''

        os.unlink(self._config_file_name(name))
        

    def get_config(self, name):
        '''
        Gets an item from the config.
        '''

        with open(self._config_file_name(name), 'rb') as f:
            return f.read()
   
              
    @property
    def config_names(self):
        '''
        Returns all item names from the config.
        '''

        return [f for f in os.listdir(self.config_folder) \
                if os.path.isfile(os.path.join(self.config_folder, f))]

    
