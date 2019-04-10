lxd-container-utils
===================

Introduction
----------------

`lxd_container_api` is python library and command line utility use in lxd container to privide an extensible unified API for interacting with applications. eg:

   - start
   - stop
   - get status
   - add user
   - drop user

and finding out container properties like:

   - ports the container listens to
 

Installation
---------------


	pip3 install git+https://github.com/MarcoDuiker/lxd_container_api.git
        

Usage
--------

This lib can be used directly from the command line with:

	lxd_container_api appname command

eg:

	lxd_container_api sshd is_running

It can also be imported in Python, eg:

	import lxd_container_api
	from lxd_container_api import apps
	apps.sshd.sshd().is_running


Extend
------

Apps can be added to the `apps` module. 

When adding an app, make sure that both the file name and class name are the same.

eg. `sshd.py` contains the class `sshd`.

Of course, you can add more classes, but those won't be accessible as an app. 

Please create a pull request to make your app available to others.