"""
A simple program for numbering images with changing the name and preserving the 
image extension, then transferring the images to another disk in the same order
"""
import os 
import shutil 
class photos:

    def new_renames(self,path):# Rename images with numbering
          self.path = path
          i = 0
          os.chdir(self.path)
          images = [file for file in os.listdir() if file.endswith(('JPEG','jpeg','PNG','png','JPG' ,'jpg')) ] # Types of image attachments 
          r = []
          for f in images: # loops is photos
                 r.append(f)
                 i += 1
                 if  r[0] != f.startswith(str(i)+'  # poto.jpg'):
                     if not  f[:2].isnumeric() or f.isalnum():
                            if 'jpg' in f or 'JPG' in f:  # If this extension is present in the file, rename the image with the numbering and keep the existing extension
                                   os.renames(f,str(i)+'  # poto.jpg')

                            elif 'PNG' in f or  'png' in f:
                                   os.renames(f,str(i)+'  # poto.PNG')

                            elif 'jpeg' in f or 'JPEG' in f:
                                   os.renames(f,str(i)+'  # poto.jpeg')
                 else:
                        return 'Pictures are numbered !! '
          return ('done successfully')

    def move_potos(self,new_path): # Move photos to another file or drive
        self.new_path = new_path

        images = [file for file in os.listdir() if file.endswith(('JPEG', 'jpeg', 'PNG', 'png', 'JPG', 'jpg'))]

        try:
                os.chdir(self.path)  # old paths
                for f in images:
                        shutil.move(f,self.new_path) #   new paths

        except NameError as erro:
                return erro
        return ('done successfully')
                
m = photos()
# print(m.new_renames('old_path'))
# print(m.move_potos('new_path'))
