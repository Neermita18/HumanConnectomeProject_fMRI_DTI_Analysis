import os
import zipfile

def extract_zip_files(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.zip'):
                zip_file_path = os.path.join(root, file)
                folder_name = file.replace('.zip', '')
                extract_path = os.path.join(root, folder_name)
                os.makedirs(extract_path, exist_ok=True)

                with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
                    zip_ref.extractall(extract_path)

                print(f"Extracted: {zip_file_path} to {extract_path}")

                # Remove the ZIP file after extraction
                os.remove(zip_file_path)
                print(f"Removed ZIP file: {zip_file_path}")


          
folder_path = 'D:\images'  
extract_zip_files(folder_path)