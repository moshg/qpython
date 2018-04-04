import os.path, sys, subprocess


if not(os.path.exists(f'{sys.prefix}/bin/pip')):
    print('You need to install pip first.')
print('Input pip commands, ie: pip install {module}')
while(True):
    cmd=input("-->")
    if not cmd: break;
    try:
        subprocess.run((f'{sys.executable} {sys.prefix}/bin/{cmd}').split())
    except FileNotFoundError as e:
        print(f'{cmd}: Invalid input')
