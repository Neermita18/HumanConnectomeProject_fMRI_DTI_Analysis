import os
import zipfile
import gzip
import shutil
def extract_zip_files_in_subfolders(base_folder):
    patient_folders = [os.path.join(base_folder, d) for d in os.listdir(base_folder) if os.path.isdir(os.path.join(base_folder, d))]

    for patient_folder in patient_folders:
        # Get the subfolder inside each patient folder (e.g., 102008)
        subfolders = [os.path.join(patient_folder, sf) for sf in os.listdir(patient_folder) if os.path.isdir(os.path.join(patient_folder, sf))]
        
        for subfolder in subfolders:
            # Define the specific subfolders to look into within each patient subfolder
            target_subfolders = ['MNINonLinear/Results/tfMRI_EMOTION_RL', 'MNINonLinear/Results/tfMRI_EMOTION_LR']

            for target_subfolder in target_subfolders:
                full_target_path = os.path.join(subfolder, target_subfolder.replace('/', os.sep))
                print(full_target_path)
                if os.path.exists(full_target_path):
                    print(f"Path exists: {full_target_path}")  # Debug statement
                    for root, dirs, files in os.walk(full_target_path):
                        print(f"Walking through {root}")  # Debug statement
                        for file in files:
                            if file == "tfMRI_EMOTION_RL.nii.gz" or file == "tfMRI_EMOTION_LR.nii.gz":
                                nii_gz_file_path = os.path.join(root, file)
                                nii_file_path = os.path.join(root, file[:-3])  # Remove ".gz" extension

                                try:
                                    # Extract the .nii.gz file
                                    with gzip.open(nii_gz_file_path, 'rb') as f_in, open(nii_file_path, 'wb') as f_out:
                                        shutil.copyfileobj(f_in, f_out)
                                    
                                    print(f"Extracted {nii_gz_file_path} to {nii_file_path}")

                                except Exception as e:
                                    print(f"Error extracting {nii_gz_file_path}: {e}")

                else:
                    print(f"Path does not exist: {full_target_path}")  # Debug statement
                
                            
                        
                    
               
            
        
       



extract_zip_files_in_subfolders('D:\images')