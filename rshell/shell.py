#from fabric.decorators import hosts
#from fabric.context_managers import settings
from fabric.api import *

def shell(host_name, host_address, user=None):
	if user != None:
		env.user = user
	FabricShell().run(host_name, host_address)
	
def issue(command, hosts, user=None):
	env.hosts = hosts
	if user != None:
		env.user = user
	for h in env.hosts:
		env.host_string = h
		FabricShell().run_cmd(command, h)

class FabricShell(object):
	_prompt = "fabric::{}> "
	_host_name = 'default'
	
	def _make_prompt(self):
		return self._prompt.format(self._host_name)
		
	def run(self, host_name, host_address):
		self._host_name = host_name
		while True:
			line = raw_input(self._make_prompt())
			
			#
			# checking first char to see if we are running a special command
			#
			if line.strip() == "":
				continue
			elif line[0] == ".":
				parts = line.split()
				if len(parts) == 1:
					continue
				
				if parts[0] == ".sudo":
					self.run_cmd(line.replace(".sudo", ""), host_address, opt="sudo")
				
			elif line.strip() == "help":
				print "Type 'quit' or 'exit' for exit the fabric shell"
				
			elif line.strip() == "quit" or line.strip() == "exit":
				break
			else:
				self.run_cmd(line, host_address)

	def run_cmd(self, cmd, host_name, **kwargs):
		with settings(host_string = host_name):
			if kwargs.has_key('opt') and kwargs['opt'] == "sudo":
				sudo(cmd)
			else:
				run(cmd)