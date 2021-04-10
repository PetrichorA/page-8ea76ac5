import os
import subprocess
from uuid import uuid4

os.chdir(os.path.dirname(os.path.abspath(__file__)))

subprocess.run(args=('wsl', 'git', 'add', '--all'))
result = subprocess.run(args=('wsl', 'git', 'commit', '-m',
                              str(uuid4())), capture_output=True).stdout
# subprocess.run(args=('wsl', 'git', 'push'))
# os.system('wsl git push')
subprocess.run('wsl git rev-parse HEAD')
# os.system('wsl git gc')
