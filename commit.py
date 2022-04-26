import os
import subprocess
from uuid import uuid4

os.chdir(os.path.dirname(os.path.abspath(__file__)))

gfw = subprocess.check_output(
    args=('python', '-u', r'C:\Users\joefa\Desktop\WorkSpace\git.py')).decode().strip()

subprocess.run(args=(gfw, 'add', '--all'))
subprocess.run(args=(gfw, 'commit', '-m', str(uuid4())))
subprocess.run(args=(gfw, 'push'))
subprocess.run(args=(gfw, 'gc'))

commit_hash = subprocess.check_output(
    args=(gfw, 'rev-parse', 'HEAD')).decode().strip()
input('https://cdn.jsdelivr.net/gh/PetrichorA/page-8ea76ac5@{}/'.format(commit_hash))
