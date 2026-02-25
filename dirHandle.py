import os

#  Make a dir
# os.mkdir('new2')
#  Create a file inside the dir
# with open('new2/test.text', 'w') as file:
#     file.write('Hello World')

#  Get List Dir
# dit_items = os.listdir('.')
# print(dit_items)


#  Rename a dir
# os.rename('new', 'new_new')


#  Remove/ Delete a Dir
# os.remove('new_new/test.text')
# os.rmdir('new_new')


#  Get File list from a dir
fileList = os.listdir('new2')
# Access each file
# for file_name in fileList:
#     print(file_name)


#  Delete Each file
for file_name in fileList:
    os.remove('new2/' + file_name)













