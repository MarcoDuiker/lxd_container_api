import subprocess

def _execute(self, command):
    '''
    Accepts command as a list, and executes using subproces.
    '''

    result = subprocess.run(command, 
                            stdout = subprocess.PIPE, 
                            stderr = subprocess.PIPE,
                            check = True)
    return result

def active():

    '''
    Uses netstat to discover port numbers the container listens to.
    
    Works only in a privileged container.
    '''
    
    # netstat -l -t --numeric-ports -p
    d = {}
    result = _execute(['netstat', '-l', '-t', '--numeric-ports', '-p'])
    if result and result.exit_code == 0:
        for row in result.stdout.split('\n')[2:-1]:
            port = row.split()[3].split(':')[-1]
            app =  row.split()[6].split('/')[-1]
            d[port] = app
    return d
