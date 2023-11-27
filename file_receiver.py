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

    if file.filename == '':
        return 'No selected file'

    destination_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(destination_path)
    return 'File uploaded successfully'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
