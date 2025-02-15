import os
# if chdir and rmdir are working,parallelly then it get a error because of rmdir is not working(The process cannot access the file because it is being used by another process: 'c:\\newdir')
print(os.getcwd())      # get the current working directory

# os.mkdir("c:\\newdir")  # create a new directory
# os.chdir("c:\\newdir")    # change the current working directory
print(os.getcwd())

os.rmdir("c:\\newdir")    # remove the directory