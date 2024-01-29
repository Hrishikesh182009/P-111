import os
import shutil

from_dir = 'C:/Users/Admin/Downloads/P-111'
to_dir = 'C:/Users/Admin/Documents/Document_Files'

list_of_files = os.listdir(from_dir)
print(list_of_files)

for ele in list_of_files:
    source,ext = os.path.splitext(list_of_files)
