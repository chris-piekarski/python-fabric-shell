from fabric.decorators import hosts
from fabric.context_managers import settings
from fabric.api import *

import readline

def shell(host_name):
	FabricShell().run(host_name)
	
def issue(command, host_name):
	FabricShell().run_cmd(command, host_name)

class FabricShell(object):
	prompt = 'fabric::> '
		
	def run(self, host_name):
		self._host = host_name
		while True:
			line = raw_input(self.prompt)
			
			#
			# checking first line if we are running a special command
			#
			if line.strip() == "":
				continue
			elif line[0] == ".":
				parts = line.split()
				if len(parts) == 1:
					continue
				
				if parts[0] == ".sudo":
					self.run_cmd(line.replace(".sudo", ""), opt="sudo")
				
			elif line.strip() == "quit" or line.strip() == "exit":
				break
			else:
				self.run_cmd(line)


	def run_cmd(self, cmd, host_name, **kwargs):
		env.user = env.local_user
		with settings(host_string = host_name):
			if kwargs.has_key('opt') and kwargs['opt'] == "sudo":
				sudo(cmd)
			else:
				run(cmd)