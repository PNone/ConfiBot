import os
import shutil
import json


with open('config.json', encoding='utf-8') as json_file:
    config = json.load(json_file)


directory = os.path.join('out', config['profileName'])
if not os.path.exists(directory):
    print("Error: images directory not found in out dir")
    exit(1)


# iterate over files in
# that directory
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if not os.path.isfile(f) or not filename.endswith('.jpg'):
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
    shutil.copy2(f, os.path.join(post_path, file_final_path))
