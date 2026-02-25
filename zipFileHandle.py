import zipfile
import  shutil

# Create a ZipFile
"""
with zipfile.ZipFile('new.zip', 'w') as zip:
    #Add File into ZipFile
    zip.write('test/new2.text')
    """

#  Extract / Red a ZipFile

"""
with zipfile.ZipFile('new.zip', 'r') as zip:
    #  Extract All
    zip.extractall()
    extracted_files = zip.namelist()
    print(extracted_files)
"""

#  Make a dir direct Zip using Shutil
shutil.make_archive('new_zip_shutil', 'zip', 'test')
















