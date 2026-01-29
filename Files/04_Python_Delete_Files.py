import shutil
from os import remove, rmdir, getcwd


remove("demo.txt")
f = open("demo.txt", "x")
f.close()
print(getcwd())
shutil.rmtree("../xtra")
print('removed')
