#import pdb Removed this and line 7 below for hte pdb (Python Debugger) so we can call hte debugger when we are opening hte file

def map(func, values):
    output_values =[]
    index = 0
    while index < len(values):
        #pdb.set_trace()
        output_values.append(func(values[index]))
        index += 1
    return output_values

def add_one(val):
    return val + 1

print(map(add_one, list(range(10))))
