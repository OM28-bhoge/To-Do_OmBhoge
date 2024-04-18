import os
from werkzeug.utils import secure_filename

# Function to handle file uploads
def upload_file(file, upload_folder):
    """Upload file to the specified folder."""
    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join(upload_folder, filename)
        file.save(file_path)
        return file_path
    else:
        return None

# Function to delete a file
def delete_file(file_path):
    """Delete file from the filesystem."""
    if os.path.exists(file_path):
        os.remove(file_path)
        return True
    else:
        return False
