#!/usr/bin/env python

#  Copyright (c) 2005, Corey Goldberg
#
#  TelnetController.py is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
 

from telnetcontroller import TelnetController, ConnectionFailed
import argparse
import getpass

class Easytel:
	def __init__(self, host, login, password, expect):
		"""
			Class constructor
			
			*host = name/IP of target machine
			*login = login ID of target machine
			*password = password for login ID of target machine
			*expect = prompt character for telnetlib class to expect
		"""
		self.telnet = TelnetController(host, login, password, expect)
		self.telnet.login()
		
	def talk(self, command):
		"""
			Function that relays commands to telnet machine. 
			
			*command = string or list of strings of commands for host machine to run
			
			Returns list of tuples where 
				* t[0] = command run
				* t[1] = console output from command
		"""
		if type(command) is not list: command = [ command ]
		
		history = []
		for cmd in command:
			history.append((cmd, self.telnet.run_command(cmd)))
		return history
		
	def hangup(self):
		self.telnet.logout()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='A handier method of handling telnet sessions in Python.')
    parser.add_argument("host", type=str,
                        help="target host to log into; can be IP or host name")
    parser.add_argument("login", type=str,
                        help="login ID to target host")
    parser.add_argument("-p", "--password", dest='password',
                        help="host machine password; omit for prompt")
    parser.add_argument("-x", "--expect", type=str, default="$", dest='expect'
                        help="expected prompt character (default is '$')")
    parser.add_argument("cmd", type=str,
                        help="command to run inside telnet unit")
	
						
    args = parser.parse_args()
    if args.password is None:
        args.password = getpass.getpass('Enter password for %s@%s:' % (args.login, args.host))

    tn = Easytel(args.host, args.login, args.password, args.expect)
	print tn.talk(args.cmd)[1]
	tn.hangup()
