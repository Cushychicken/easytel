#!/usr/bin/env python

#  Copyright (c) 2005, Corey Goldberg
#
#  TelnetController.py is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
 

from telnetcontroller import TelnetController
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='A handier method of handling telnet sessions in Python.')
    args = parser.parse_args()
    print args.echo
