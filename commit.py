import os
import subprocess
from uuid import uuid4

os.chdir(os.path.dirname(os.path.abspath(__file__)))

subprocess.run(r'wsl git add --all')
subprocess.run(args=('wsl', 'git', 'commit', '-m', str(uuid4())))
# os.system(r'wsl git commit -m "{}"'.format(uuid4()))
# os.system('wsl git push')
subprocess.run('wsl git rev-parse HEAD')
# os.system('wsl git gc')
