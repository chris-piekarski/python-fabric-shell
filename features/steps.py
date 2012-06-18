from lettuce import *
import rshell
import tempfile
import os

from fabric.api import *

world.host = None

#fabric api config
env.use_ssh_config = True
env.no_keys = True

@step('I connect to (.*)')
def connect_ssh_host(step, host_name):
	world.host = host_name
	rshell.issue(host_name)
		
@step('I issue (.*) command to (.*)')
def issue_command(step, command, host_name):
	try:
		rshell.issue(command, host_name)
	except Exception as e:
		assert True == False, \
			"Command threw '{}'".format(e)