#@PydevCodeAnalysisIgnore
#'Mine' is a configured client side SSH host
#Replace with appropriate host name
Feature: Test RShell
	Provide confidence that rshell works
	Scenario: Connect to SSH host and issue commands
		Given I issue uname -a command to Mine
		Given I issue whoami command to Mine
		Given I issue ls command to Mine
		Given I issue 'blah' command to Mine