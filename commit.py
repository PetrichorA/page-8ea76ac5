import os
from uuid import uuid4

os.chdir(os.path.dirname(os.path.abspath(__file__)))

os.system('wsl git add --all')
os.system(r'wsl git commit -m "{}"'.format(uuid4()))
os.system('wsl git push')
os.system('wsl git gc')
