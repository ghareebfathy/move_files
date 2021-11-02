"""
    A small program to transfer files by file type to folders 
    with the same name
"""

import  os
import  shutil


print(os.getcwd())
for  filename in  os.listdir():
    # Sound 
    if filename.endswith('.mp3'): #Add file extension by type
        if not  os.path.exists('Sound'):
            os.mkdir('Sound') # Create a Sound folder
        shutil.copy(filename,'Sound') # Copy the files to the folder
        os.remove(filename) # After copying, delete the files
    # photos
    if filename.endswith('jpg')or filename.endswith('png')or filename.endswith('JPEG'):
        if not  os.path.exists('photo'):
            os.mkdir('photo')
        shutil.copy(filename,'photo')
        os.remove(filename)
    # Books
    if filename.endswith('pdf'):
        if not  os.path.exists('Books'):
            os.mkdir('Books')
        shutil.copy(filename,'Books')
        os.remove(filename)
    # apps
    if filename.endswith('dmg'):
        if not os.path.exists('app'):
            os.mkdir('app')
        shutil.copy(filename, 'app')
        os.remove(filename)

    # potoshop
    if filename.endswith('psd'):
        if not  os.path.exists('potoshop'):
            os.mkdir('potoshop')
        shutil.copy(filename,'potoshop')
        os.remove(filename)
print('Empty Files') # Confirmation that the file is empty

