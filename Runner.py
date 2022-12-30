import os
import random
import string
import wget
'--------------------------'
letters = string.ascii_lowercase
''.join(random.choice(letters) for i in range(10))
path = os.environ.get('LOCALAPPDATA')
imports = ['keyboard','mouse','random','time','wget',]
imports2 = ['keyboard-','mouse-','random-','time-','wget-']
a = -1
remote_url = 'https://raw.githubusercontent.com/tygoz/pyclicker/main/autoclicker.py'
local_file = '{''.join(random.choice(letters) for i in range(10))}.txt'
'--------------------------'
try:
    listy = str(os.listdir(f'{path}/Programs/Python/Python310/Lib/site-packages'))
except:
    listy = str(os.listdir(f'{path}/Programs/Python/Python39/Lib/site-packages'))
for a in imports:
    b = 0
    if not imports[a] in listy:
        b = 1
    if not imports2[a] in listy:
        b = 1
    if b == 1:
        b = 0
        os.system(f"pip install {imports[a]}")
wget.download(remote_url, local_file)
f = open(local_file, "r")
file = f.read()
f.close()
os.remove(local_file)
print('')
exec(file)

'''
if the file doesn't download replace it with the code below

-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-

import requests
response = requests.get(remote_url)
f = open(local_file, "wb").write(response.content)
file = f.read()
f.close()
os.remove(local_file)

-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
'''
