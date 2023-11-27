from flask import Flask, request
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'received_files'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # Ensure the destination directory exists

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'

    file = request.files['file']
    folder_name = request.form.get('folder_name', '')  # Get the folder name from the request

    if folder_name:
        destination_path = os.path.join(app.config['UPLOAD_FOLDER'], folder_name, file.filename)
    else:
        destination_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)

    file.save(destination_path)
    return 'File uploaded successfully'

@app.route('/upload', methods=['POST'])
def create_folder():
    folder_name = request.form.get('folder_name', '')

    if folder_name:
        folder_path = os.path.join(app.config['UPLOAD_FOLDER'], folder_name)
        os.makedirs(folder_path, exist_ok=True)
        return 'Folder created successfully'

    return 'Invalid folder name'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
