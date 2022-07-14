import subprocess
# import required module
import os
import shutil
import json

with open('config.json') as json_file:
    config = json.load(json_file)


process = subprocess.run(f'cmd /c python -m instaloader {config["profileName"]} -l {config["username"]} -p {config["password"]} --no-profile-pic')

# assign directory
directory = config['profileName']
if not os.path.exists(directory):
    os.mkdir(directory)

# iterate over files in
# that directory
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if not os.path.isfile(f):
        continue
    elif not filename.endswith('.jpg'):
        os.remove(f)
        continue

    post_name, file_final_path = filename.split('_UTC')

    post_path = os.path.join(directory, post_name)
    # checking if it is a file
    if not os.path.exists(post_path):
        os.mkdir(post_path)
    if file_final_path == '.jpg':
        file_final_path = '1.jpg'
    else:
        file_final_path = file_final_path[1::]
    shutil.move(f, os.path.join(post_path, file_final_path))
