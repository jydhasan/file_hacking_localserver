import requests
import os
import shutil

url = "http://10.5.225.148:5000/upload"  # Replace with the destination computer's IP address and port

source_folder = r'C:\Users\jyfhasan\Pictures\Screenshots'
destination_folder = 'screenshots'  # The folder name on the destination server

# Ensure the destination folder exists on the server
response = requests.post(url, data={'action': 'create_folder', 'folder_name': destination_folder})
print(response.text)

# Iterate through files in the source folder and send each file
for filename in os.listdir(source_folder):
    if filename.lower() == 'desktop.ini':
        continue  # Skip 'desktop.ini' file

    source_file_path = os.path.join(source_folder, filename)
    destination_file_path = os.path.join(destination_folder, filename)

    print(f"Copying file: {source_file_path} to {destination_file_path}")

    shutil.copyfile(source_file_path, destination_file_path)

    files = {'file': open(destination_file_path, 'rb')}
    response = requests.post(url, files=files, data={'action': 'upload', 'folder_name': destination_folder})
    print(response.text)
