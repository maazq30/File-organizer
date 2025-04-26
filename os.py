import os
import shutil

# Take input for the source directory
source_dir = input("Enter the path of the folder you want to organize: ")

# Check if the directory exists
if not os.path.isdir(source_dir):
    print("The specified directory does not exist. Please check the path and try again.")
    exit()

# Define file type categories
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Music": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".7z", ".tar"],
    "Scripts": [".py", ".js", ".html", ".css"],
    "Others": []  
}

# Create folders for each category if not already present
for folder in file_types.keys():
    folder_path = os.path.join(source_dir, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Organize files
for filename in os.listdir(source_dir):
    file_path = os.path.join(source_dir, filename)
    
    # Skip directories
    if os.path.isdir(file_path):
        continue

    # Get file extension
    _, ext = os.path.splitext(filename)
    moved = False

    # Check and move files into appropriate folders
    for folder, extensions in file_types.items():
        if ext.lower() in extensions:
            shutil.move(file_path, os.path.join(source_dir, folder, filename))
            moved = True
            break

    # Move to 'Others' if extension not matched
    if not moved:
        shutil.move(file_path, os.path.join(source_dir, "Others", filename))

print("Files organized successfully.")
