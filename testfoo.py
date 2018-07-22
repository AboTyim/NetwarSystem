import psutil
import getpass
for p in psutil.process_iter(attrs=['name', 'username']):
        if (p.info['username'] == getpass.getuser()) and (p.info['name'] == "foo"):
                print("running")
