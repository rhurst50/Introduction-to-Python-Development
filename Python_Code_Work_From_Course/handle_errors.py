''' This was the original
my_file = open('recipies.txt', 'x')

my_file.write('Meaballs\n')
my_file.close()'''

import sys
file_name = 'recipies.txt'

try:
    my_file = open(file_name, 'x')
    my_file.write('Meaballs\n')
    my_file.close()
except:
    print(f"The {file_name} files already exists...idiot\nSo go fuck yourself in the butthole!!")
    sys.exit(1)
else:
    print(f"Wrote to {file_name} successfully")
finally:
    print("....................Python File Function Completed......................")
