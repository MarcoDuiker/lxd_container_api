#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
This is the command line interface to lxd_container_api.
'''

import argparse
import os
import sys


# make sure we can import the package when run as script
if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
    
import lxd_container_api
from lxd_container_api import apps


def main():
    '''
    The main entrypoint for the command line.
    '''
    
       
    parser = argparse.ArgumentParser(description = 'lxd_container_api')
    parser.add_argument("app", help = "The app.")
    parser.add_argument("command", help = "The command to execute, or property to get.")
    parser.add_argument("parameters", nargs=argparse.REMAINDER, help = "All required and optional parameters")
    
    args = parser.parse_args()

    module = getattr(apps, args.app)
    app = getattr(module, args.app)
    app_instance = app()
    if callable(getattr(app, args.command)):
        fn_to_run = getattr(app, args.command)
        return str(fn_to_run(*args.parameters))
    else:
        return str(getattr(app_instance, args.command))
               

if __name__ == "__main__":
    '''
    This script is invoked from command line.
    Switch to main entry point and report results to the console.
    '''
    
    result = main()
    sys.stdout.write(result)
