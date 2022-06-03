import os
path = os.environ.get('LOCALAPPDATA')
imports = ['keyboard','mouse','random','time','wget', 'requests']
imports2 = ['keyboard-','mouse-','random-','time-','wget-','requests-']
a = -1
try:
    listy = str(os.listdir(f'{path}\Programs\Python\Python39\Lib\site-packages'))
except:
    listy = str(os.listdir(f'{path}\Programs\Python\Python310\Lib\site-packages'))
while not 3 == a:
    b = 0
    a = a + 1
    if imports[a] in listy:
        pass
    else:
        b = 1
    if imports2[a] in listy:
        pass
    else:
        b = 1
    if b == 1:
        b = 0
        os.system(f"pip install {imports[a]}")
remote_url = 'https://raw.githubusercontent.com/tygoz/pyclicker/main/autoclicker.py'
local_file = 'click.txt'

try:
    import wget
    wget.download(remote_url, local_file)
    f = open(local_file, "r")
    file = f.read()
    f.close()
    os.remove(local_file)
except:
    import requests
    response = requests.get(remote_url)
    f = open(local_file, "wb").write(response.content)
    file = f.read()
    f.close()
    os.remove(local_file)
print('')
exec(file)
