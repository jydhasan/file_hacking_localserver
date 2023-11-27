import requests
import os
import shutil

url = "http://10.5.225.148:5000/upload"  # Replace with the destination computer's IP address and port

source_file_path = r'C:\Users\jyfhasan\Pictures\Screenshots\zahid.png'
destination_file_path = os.path.join(os.path.dirname(__file__), 'zahid.png')

shutil.copyfile(source_file_path, destination_file_path)

files = {'file': open(destination_file_path, 'rb')}
response = requests.post(url, files=files)

print(response.text)
