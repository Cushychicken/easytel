easytel
=======

A simplified interface for telnet sessions in Python. Usable as a command line interface or as an easily importable end user class.

### In Python
```python
from easytel import Easytel
ez = Easytel(HOST, LOGIN, PSWD, EXPECT) # takes host name, login ID, password, and prompt char as inputs
result = ez.talk([ 'date', 'ls -al'])   # takes list of strings as input
                                        # returns tuple of (command, command_output)

```

### In Shell
```shell
# Will be prompted for a password if not entered in the shell
python easytel.py 192.168.1.1 home $ 
```

Inspired by and derived from Corey Goldberg's [TelnetController.py script](http://goldb.org/telnetpython.html) 
that you can find on [his website](http://goldb.org/). 
