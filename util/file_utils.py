import os

def save_uploaded_file(uploaded_file, upload_dir="data"):
    os.makedirs(upload_dir, exist_ok=True)
    filepath = os.path.join(upload_dir, uploaded_file.name)
    with open(filepath, "wb") as f:
        f.write(uploaded_file.getbuffer())
    return filepath
