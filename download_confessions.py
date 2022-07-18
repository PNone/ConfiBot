import subprocess
# import required module
import os
import shutil
import json

with open('config.json', encoding='utf-8') as json_file:
    config = json.load(json_file)


process = subprocess.run(f'cmd /c python -m instaloader {config["profileName"]} -l {config["username"]} -p {config["password"]} --no-profile-pic')

# assign directory
directory = os.path.join('out', config['profileName'])
if not os.path.exists('out'):
    os.mkdir('out')

shutil.move(config['profileName'], 'out')
