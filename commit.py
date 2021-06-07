import os
import subprocess
from uuid import uuid4

os.chdir(os.path.dirname(os.path.abspath(__file__)))

subprocess.run(args=('wsl', 'git', 'add', '--all'))
subprocess.run(args=('wsl', 'git', 'commit', '-m', str(uuid4())))
subprocess.run(args=('wsl', 'git', 'push'))
subprocess.run(args=('wsl', 'git', 'gc'))

commit_hash = subprocess.run(
    args=('wsl', 'git', 'rev-parse', 'HEAD'),
    capture_output=True).stdout.decode().strip()
input('https://cdn.jsdelivr.net/gh/PetrichorA/page-648446cf@{}/'.format(commit_hash))
