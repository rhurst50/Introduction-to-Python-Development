my_file = open('xmen.txt', 'w+')
my_file.write('Beast\n')
my_file.write('Phoenix\n')
my_file.writelines([
        'Cyclops\n',
        'Bishop\n',
        'Nightcrawler\n',
])

my_file.close()

my_file = open('xmen.txt', 'r')
print(my_file.read())
print("I am reading again!")
my_file.seek(0)
print(my_file.read())
my_file.close()

#alternate way to not have to close is by calling 'with'

with open('xmen.txt', 'w+') as my_file:
    my_file.write('Beast\n')
    my_file.write('Phoenix\n')
    my_file.writelines([
        'Cyclops\n',
        'Bishop\n',
        'Nightcrawler\n',
])

my_file.close()

my_file = open('xmen.txt', 'r')
print(my_file.read())
print("I am reading again!")

my_file.seek(0)
print(my_file.read())
my_file.close()

