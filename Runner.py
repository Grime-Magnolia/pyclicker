import os
path = os.environ.get('%LOCALAPPDATA%')
imports = ['keyboard','mouse','random','time','wget']
imports2 = ['keyboard-','mouse-','random-','time-','wget-']
a = -1
listy = str(os.listdir(f'{path}/Programs/Python/Python39/Lib/site-packages/'))
while not 3 == a:
    b = 0
    a = a + 1
    if imports[a] in listy:
    else:
        b = 1
    if imports2[a] in listy:
    else:
        b = 1
    if b == 1:
        b = 0
        os.system(f"pip install {imports[a]}")
import wget
remote_url = 'https://raw.githubusercontent.com/tygoz/pyclicker/main/autoclicker.py'
local_file = 'click.txt'
wget.download(remote_url, local_file)
f = open("click.txt", "r")
file = f.read()
f.close()
os.remove("click.txt")
print('')
exec(file)
