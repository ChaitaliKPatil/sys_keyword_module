#Interrogating the system
import sys
import keyword as k
print('Python Version: ',sys.version)
print(' display the actual location of the Python interpreter on your system ',sys.executable)
print(' a list of all directories where the Python interpreter looks for module files ==Python Module Search Path: ')
for d in sys.path:
    print(d)
print(k.kwlist)
print(k.iskeyword('and'))

help(sys)
