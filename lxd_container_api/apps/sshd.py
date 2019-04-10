from ._app import _app

class sshd(_app):
    import crypt

    def __init__(self):
        self.name = 'sshd'

    def set_password(self, username, password):
        '''Sets the password for an existing user.'''
        
        return self._execute(['usermod',  '-p', crypt.crypt(password), username],
                             universal_newlines = True)
